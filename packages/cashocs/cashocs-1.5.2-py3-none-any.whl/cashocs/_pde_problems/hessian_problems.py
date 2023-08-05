# Copyright (C) 2020-2022 Sebastian Blauth
#
# This file is part of cashocs.
#
# cashocs is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# cashocs is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with cashocs.  If not, see <https://www.gnu.org/licenses/>.

"""Abstract implementation of the Hessian problem.

This uses Krylov subspace methods to iteratively solve
the "Hessian problems" occurring in the truncated Newton
method.
"""

from __future__ import annotations

import abc
from typing import TYPE_CHECKING, List, Optional

import fenics
import numpy as np
from petsc4py import PETSc

from .._exceptions import CashocsException
from .._loggers import debug
from ..nonlinear_solvers import picard_iteration
from ..utils import _assemble_petsc_system, _setup_petsc_options, _solve_linear_problem


if TYPE_CHECKING:
    from .._forms import ControlFormHandler
    from .control_gradient_problem import ControlGradientProblem


class BaseHessianProblem(abc.ABC):
    """Base class for derived Hessian problems."""

    def __init__(
        self, form_handler: ControlFormHandler, gradient_problem: ControlGradientProblem
    ) -> None:
        """
        Parameters
        ----------
        form_handler : ControlFormHandler
            The FormHandler object for the optimization problem.
        gradient_problem : ControlGradientProblem
            The ControlGradientProblem object (this is needed for the computation
            of the Hessian).
        """

        self.form_handler = form_handler
        self.gradient_problem = gradient_problem

        self.config = self.form_handler.config
        self.gradient = self.gradient_problem.gradient

        self.inner_newton = self.config.get("AlgoTNM", "inner_newton", fallback="cr")
        self.max_it_inner_newton = self.config.getint(
            "AlgoTNM", "max_it_inner_newton", fallback=50
        )
        self.inner_newton_rtol = self.config.getfloat(
            "AlgoTNM", "inner_newton_rtol", fallback=1e-15
        )
        self.inner_newton_atol = self.config.getfloat(
            "AlgoTNM", "inner_newton_atol", fallback=0.0
        )

        self.test_directions = self.form_handler.test_directions
        self.residual = [fenics.Function(V) for V in self.form_handler.control_spaces]
        self.delta_control = [
            fenics.Function(V) for V in self.form_handler.control_spaces
        ]

        self.state_A_tensors = [
            fenics.PETScMatrix() for i in range(self.form_handler.state_dim)
        ]
        self.state_b_tensors = [
            fenics.PETScVector() for i in range(self.form_handler.state_dim)
        ]
        self.adjoint_A_tensors = [
            fenics.PETScMatrix() for i in range(self.form_handler.state_dim)
        ]
        self.adjoint_b_tensors = [
            fenics.PETScVector() for i in range(self.form_handler.state_dim)
        ]

        self.state_dim = self.form_handler.state_dim
        self.control_dim = self.form_handler.control_dim

        self.temp1 = [fenics.Function(V) for V in self.form_handler.control_spaces]
        self.temp2 = [fenics.Function(V) for V in self.form_handler.control_spaces]

        self.p = [fenics.Function(V) for V in self.form_handler.control_spaces]
        self.p_prev = [fenics.Function(V) for V in self.form_handler.control_spaces]
        self.p_pprev = [fenics.Function(V) for V in self.form_handler.control_spaces]
        self.s = [fenics.Function(V) for V in self.form_handler.control_spaces]
        self.s_prev = [fenics.Function(V) for V in self.form_handler.control_spaces]
        self.s_pprev = [fenics.Function(V) for V in self.form_handler.control_spaces]
        self.q = [fenics.Function(V) for V in self.form_handler.control_spaces]
        self.q_prev = [fenics.Function(V) for V in self.form_handler.control_spaces]

        self.hessian_actions = [
            fenics.Function(V) for V in self.form_handler.control_spaces
        ]
        self.inactive_part = [
            fenics.Function(V) for V in self.form_handler.control_spaces
        ]
        self.active_part = [
            fenics.Function(V) for V in self.form_handler.control_spaces
        ]

        self.controls = self.form_handler.controls

        self.picard_rtol = self.config.getfloat(
            "StateSystem", "picard_rtol", fallback=1e-10
        )
        self.picard_atol = self.config.getfloat(
            "StateSystem", "picard_atol", fallback=1e-12
        )
        self.picard_max_iter = self.config.getint(
            "StateSystem", "picard_iter", fallback=50
        )
        self.picard_verbose = self.config.getboolean(
            "StateSystem", "picard_verbose", fallback=False
        )

        self.no_sensitivity_solves = 0
        self.state_ksps = [
            PETSc.KSP().create() for i in range(self.form_handler.state_dim)
        ]
        _setup_petsc_options(self.state_ksps, self.form_handler.state_ksp_options)
        self.adjoint_ksps = [
            PETSc.KSP().create() for i in range(self.form_handler.state_dim)
        ]
        _setup_petsc_options(self.adjoint_ksps, self.form_handler.adjoint_ksp_options)

        # Initialize the PETSc Krylov solver for the Riesz projection problems
        self.ksps = [PETSc.KSP().create() for i in range(self.control_dim)]

        option = [
            ["ksp_type", "cg"],
            ["pc_type", "hypre"],
            ["pc_hypre_type", "boomeramg"],
            ["pc_hypre_boomeramg_strong_threshold", 0.7],
            ["ksp_rtol", 1e-16],
            ["ksp_atol", 1e-50],
            ["ksp_max_it", 100],
        ]
        self.riesz_ksp_options = []
        for i in range(self.control_dim):
            self.riesz_ksp_options.append(option)

        _setup_petsc_options(self.ksps, self.riesz_ksp_options)
        for i, ksp in enumerate(self.ksps):
            ksp.setOperators(self.form_handler.riesz_projection_matrices[i])

    def hessian_application(
        self, h: List[fenics.Function], out: List[fenics.Function]
    ) -> None:
        r"""Computes the application of the Hessian to some element

        This is needed in the truncated Newton method where we solve the system

        .. math:: J''(u) [\Delta u] = - J'(u)

        via iterative methods (conjugate gradient or conjugate residual method)

        Parameters
        ----------
        h : list[fenics.Function]
            A function to which we want to apply the Hessian to.
        out : list[fenics.Function]
            A list of functions into which the result is saved.

        Returns
        -------
        None
        """

        for i in range(self.control_dim):
            self.test_directions[i].vector().vec().aypx(0.0, h[i].vector().vec())

        self.states_prime = self.form_handler.states_prime
        self.adjoints_prime = self.form_handler.adjoints_prime
        self.bcs_list_ad = self.form_handler.bcs_list_ad

        if not self.form_handler.state_is_picard or self.form_handler.state_dim == 1:

            for i in range(self.state_dim):
                A, b = _assemble_petsc_system(
                    self.form_handler.sensitivity_eqs_lhs[i],
                    self.form_handler.sensitivity_eqs_rhs[i],
                    self.bcs_list_ad[i],
                )
                _solve_linear_problem(
                    self.state_ksps[i],
                    A,
                    b,
                    self.states_prime[i].vector().vec(),
                    self.form_handler.state_ksp_options[i],
                )
                self.states_prime[i].vector().apply("")

            for i in range(self.state_dim):
                A, b = _assemble_petsc_system(
                    self.form_handler.adjoint_sensitivity_eqs_lhs[-1 - i],
                    self.form_handler.w_1[-1 - i],
                    self.bcs_list_ad[-1 - i],
                )
                _solve_linear_problem(
                    self.adjoint_ksps[-1 - i],
                    A,
                    b,
                    self.adjoints_prime[-1 - i].vector().vec(),
                    self.form_handler.adjoint_ksp_options[-1 - i],
                )
                self.adjoints_prime[-1 - i].vector().apply("")

        else:
            picard_iteration(
                self.form_handler.sensitivity_eqs_picard,
                self.states_prime,
                self.form_handler.bcs_list_ad,
                max_iter=self.picard_max_iter,
                rtol=self.picard_rtol,
                atol=self.picard_atol,
                verbose=self.picard_verbose,
                inner_damped=False,
                inner_inexact=False,
                inner_verbose=False,
                inner_max_its=2,
                ksps=self.state_ksps,
                ksp_options=self.form_handler.state_ksp_options,
                A_tensors=self.state_A_tensors,
                b_tensors=self.state_b_tensors,
                inner_is_linear=True,
            )

            picard_iteration(
                self.form_handler.adjoint_sensitivity_eqs_picard,
                self.adjoints_prime,
                self.form_handler.bcs_list_ad,
                max_iter=self.picard_max_iter,
                rtol=self.picard_rtol,
                atol=self.picard_atol,
                verbose=self.picard_verbose,
                inner_damped=False,
                inner_inexact=False,
                inner_verbose=False,
                inner_max_its=2,
                ksps=self.adjoint_ksps,
                ksp_options=self.form_handler.adjoint_ksp_options,
                A_tensors=self.adjoint_A_tensors,
                b_tensors=self.adjoint_b_tensors,
                inner_is_linear=True,
            )

        for i in range(self.control_dim):
            b = fenics.as_backend_type(
                fenics.assemble(self.form_handler.hessian_rhs[i])
            ).vec()

            _solve_linear_problem(
                self.ksps[i],
                b=b,
                x=out[i].vector().vec(),
                ksp_options=self.riesz_ksp_options[i],
            )
            out[i].vector().apply("")

        self.no_sensitivity_solves += 2

    def newton_solve(
        self, idx_active: Optional[List[int]] = None
    ) -> List[fenics.Function]:
        """Solves the problem with a truncated Newton method.

        Parameters
        ----------
        idx_active : list[int] or None, optional
            List of active indices

        Returns
        -------
        list[fenics.Function]
            The Newton increment

        """

        self.gradient_problem.solve()
        self.form_handler.compute_active_sets()

        for j in range(self.control_dim):
            self.delta_control[j].vector().vec().set(0.0)

        if self.inner_newton == "cg":
            self.cg(idx_active)
        elif self.inner_newton == "cr":
            self.cr(idx_active)

        return self.delta_control

    @abc.abstractmethod
    def cg(self, idx_active: Optional[List[int]] = None) -> None:
        """Solves the (truncated) Newton step with a CG method

        Parameters
        ----------
        idx_active : list[int] or None, optional
            The list of active indices

        Returns
        -------
        None
        """

        pass

    @abc.abstractmethod
    def cr(self, idx_active: Optional[List[int]] = None) -> None:
        """Solves the (truncated) Newton step with a CR method

        Parameters
        ----------
        idx_active : list[int] or None, optional
            The list of active indices

        Returns
        -------
        None
        """

        pass


class HessianProblem(BaseHessianProblem):
    """PDE Problem used to solve the (reduced) Hessian problem."""

    def __init__(
        self, form_handler: ControlFormHandler, gradient_problem: ControlGradientProblem
    ) -> None:
        """Initializes self.

        Parameters
        ----------
        form_handler : ControlFormHandler
            The FormHandler object for the optimization problem.
        gradient_problem : ControlGradientProblem
            The ControlGradientProblem object (this is needed for the computation
            of the Hessian).
        """

        super().__init__(form_handler, gradient_problem)

    def reduced_hessian_application(
        self, h: List[fenics.Function], out: List[fenics.Function]
    ) -> None:
        """Computes the application of the reduced Hessian on a direction.

        This is needed to solve the Newton step with iterative solvers.

        Parameters
        ----------
        h : list[fenics.Function]
            The direction, onto which the reduced Hessian is applied
        out : list[fenics.Function]
            The output of the application of the (linear) operator

        Returns
        -------
        None
        """

        for j in range(self.control_dim):
            out[j].vector().vec().set(0.0)

        self.form_handler.restrict_to_inactive_set(h, self.inactive_part)
        self.hessian_application(self.inactive_part, self.hessian_actions)
        self.form_handler.restrict_to_inactive_set(
            self.hessian_actions, self.inactive_part
        )
        self.form_handler.restrict_to_active_set(h, self.active_part)

        for j in range(self.control_dim):
            out[j].vector().vec().aypx(
                0.0,
                self.active_part[j].vector().vec()
                + self.inactive_part[j].vector().vec(),
            )

    def newton_solve(
        self, idx_active: Optional[List[List[int]]] = None
    ) -> List[fenics.Function]:
        """Solves the Newton step with an iterative method

        Parameters
        ----------
        idx_active : list[list[int]] or None, optional
            The list of active indices

        Returns
        -------
        list[fenics.Function]
            The Newton increment
        """

        if idx_active is not None:
            raise CashocsException("Must not pass idx_active to HessianProblem.")

        return super().newton_solve()

    def cg(self, idx_active: Optional[List[int]] = None) -> None:
        """Solves the (truncated) Newton step with a CG method

        Parameters
        ----------
        idx_active : list[int] or None, optional
            The list of active indices

        Returns
        -------
        list[fenics.Function]
            The Newton increment

        """

        for j in range(self.control_dim):
            self.residual[j].vector().vec().aypx(0.0, -self.gradient[j].vector().vec())
            self.p[j].vector().vec().aypx(0.0, self.residual[j].vector().vec())

        self.rsold = self.form_handler.scalar_product(self.residual, self.residual)
        self.eps_0 = np.sqrt(self.rsold)

        for i in range(self.max_it_inner_newton):

            self.reduced_hessian_application(self.p, self.q)

            self.form_handler.restrict_to_active_set(self.p, self.temp1)
            sp_val1 = self.form_handler.scalar_product(self.temp1, self.temp1)

            self.form_handler.restrict_to_inactive_set(self.p, self.temp1)
            self.form_handler.restrict_to_inactive_set(self.q, self.temp2)
            sp_val2 = self.form_handler.scalar_product(self.temp1, self.temp2)
            sp_val = sp_val1 + sp_val2
            self.alpha = self.rsold / sp_val

            for j in range(self.control_dim):
                self.delta_control[j].vector().vec().axpy(
                    self.alpha, self.p[j].vector().vec()
                )
                self.residual[j].vector().vec().axpy(
                    -self.alpha, self.q[j].vector().vec()
                )

            self.rsnew = self.form_handler.scalar_product(self.residual, self.residual)
            self.eps = np.sqrt(self.rsnew)
            debug(f"Residual of the CG method: {self.eps/self.eps_0:.3e} (relative)")
            if self.eps < self.inner_newton_atol + self.inner_newton_rtol * self.eps_0:
                break

            self.beta = self.rsnew / self.rsold

            for j in range(self.control_dim):
                self.p[j].vector().vec().aypx(
                    self.beta, self.residual[j].vector().vec()
                )

            self.rsold = self.rsnew

    def cr(self, idx_active: Optional[List[int]] = None) -> None:
        """Solves the (truncated) Newton step with a CR method

        Parameters
        ----------
        idx_active : list[int] or None, optional
            The list of active indices

        Returns
        -------
        None
        """

        for j in range(self.control_dim):
            self.residual[j].vector().vec().aypx(0.0, -self.gradient[j].vector().vec())
            self.p[j].vector().vec().aypx(0.0, self.residual[j].vector().vec())

        self.eps_0 = np.sqrt(
            self.form_handler.scalar_product(self.residual, self.residual)
        )

        self.reduced_hessian_application(self.residual, self.s)

        for j in range(self.control_dim):
            self.q[j].vector().vec().aypx(0.0, self.s[j].vector().vec())

        self.form_handler.restrict_to_active_set(self.residual, self.temp1)
        self.form_handler.restrict_to_active_set(self.s, self.temp2)
        sp_val1 = self.form_handler.scalar_product(self.temp1, self.temp2)
        self.form_handler.restrict_to_inactive_set(self.residual, self.temp1)
        self.form_handler.restrict_to_inactive_set(self.s, self.temp2)
        sp_val2 = self.form_handler.scalar_product(self.temp1, self.temp2)

        self.rAr = sp_val1 + sp_val2

        for i in range(self.max_it_inner_newton):

            self.form_handler.restrict_to_active_set(self.q, self.temp1)
            self.form_handler.restrict_to_inactive_set(self.q, self.temp2)
            denom1 = self.form_handler.scalar_product(self.temp1, self.temp1)
            denom2 = self.form_handler.scalar_product(self.temp2, self.temp2)
            denominator = denom1 + denom2

            self.alpha = self.rAr / denominator

            for j in range(self.control_dim):
                self.delta_control[j].vector().vec().axpy(
                    self.alpha, self.p[j].vector().vec()
                )
                self.residual[j].vector().vec().axpy(
                    -self.alpha, self.q[j].vector().vec()
                )

            self.eps = np.sqrt(
                self.form_handler.scalar_product(self.residual, self.residual)
            )
            debug(f"Residual of the CR method: {self.eps/self.eps_0:.3e} (relative)")
            if (
                self.eps < self.inner_newton_atol + self.inner_newton_rtol * self.eps_0
                or i == self.max_it_inner_newton - 1
            ):
                break

            self.reduced_hessian_application(self.residual, self.s)

            self.form_handler.restrict_to_active_set(self.residual, self.temp1)
            self.form_handler.restrict_to_active_set(self.s, self.temp2)
            sp_val1 = self.form_handler.scalar_product(self.temp1, self.temp2)
            self.form_handler.restrict_to_inactive_set(self.residual, self.temp1)
            self.form_handler.restrict_to_inactive_set(self.s, self.temp2)
            sp_val2 = self.form_handler.scalar_product(self.temp1, self.temp2)

            self.rAr_new = sp_val1 + sp_val2
            self.beta = self.rAr_new / self.rAr

            for j in range(self.control_dim):
                self.p[j].vector().vec().aypx(
                    self.beta, self.residual[j].vector().vec()
                )
                self.q[j].vector().vec().aypx(self.beta, self.s[j].vector().vec())

            self.rAr = self.rAr_new
