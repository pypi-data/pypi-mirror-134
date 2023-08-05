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

"""Nonlinear CG method.

"""

from __future__ import annotations

import fenics

from .optimization_algorithm import OptimizationAlgorithm


class NonlinearCGMethod(OptimizationAlgorithm):
    def __init__(self, optimization_problem, line_search):
        super().__init__(optimization_problem)
        self.line_search = line_search

        self.gradient_prev = [
            fenics.Function(V) for V in self.form_handler.control_spaces
        ]
        self.difference = [fenics.Function(V) for V in self.form_handler.control_spaces]
        self.temp_HZ = [fenics.Function(V) for V in self.form_handler.control_spaces]

        self.cg_method = self.config.get("AlgoCG", "cg_method", fallback="FR")
        self.cg_periodic_restart = self.config.getboolean(
            "AlgoCG", "cg_periodic_restart", fallback=False
        )
        self.cg_periodic_its = self.config.getint(
            "AlgoCG", "cg_periodic_its", fallback=10
        )
        self.cg_relative_restart = self.config.getboolean(
            "AlgoCG", "cg_relative_restart", fallback=False
        )
        self.cg_restart_tol = self.config.getfloat(
            "AlgoCG", "cg_restart_tol", fallback=0.25
        )

        self.memory = 0

    def run(self):

        self.initialize_solver()
        self.memory = 0

        while True:
            self.store_previous_gradient()

            self.compute_gradient()
            self.gradient_norm = self.compute_gradient_norm()
            self.compute_beta()

            if self.convergence_test():
                break

            self.compute_search_direction()
            self.restart()
            self.project_ncg_search_direction()
            self.check_for_ascent()

            self.objective_value = self.cost_functional.evaluate()
            self.output()

            self.line_search.perform(
                self, self.search_direction, self.has_curvature_info
            )

            self.iteration += 1
            if self.nonconvergence():
                break

    def compute_beta(self) -> None:

        if self.iteration > 0:
            if self.cg_method == "FR":
                self.beta_numerator = self.form_handler.scalar_product(
                    self.gradient, self.gradient
                )
                self.beta_denominator = self.form_handler.scalar_product(
                    self.gradient_prev, self.gradient_prev
                )
                self.beta = self.beta_numerator / self.beta_denominator

            elif self.cg_method == "PR":
                for i in range(len(self.gradient)):
                    self.difference[i].vector().vec().aypx(
                        0.0,
                        self.gradient[i].vector().vec()
                        - self.gradient_prev[i].vector().vec(),
                    )

                self.beta_numerator = self.form_handler.scalar_product(
                    self.gradient, self.difference
                )
                self.beta_denominator = self.form_handler.scalar_product(
                    self.gradient_prev, self.gradient_prev
                )
                self.beta = self.beta_numerator / self.beta_denominator

            elif self.cg_method == "HS":
                for i in range(len(self.gradient)):
                    self.difference[i].vector().vec().aypx(
                        0.0,
                        self.gradient[i].vector().vec()
                        - self.gradient_prev[i].vector().vec(),
                    )

                self.beta_numerator = self.form_handler.scalar_product(
                    self.gradient, self.difference
                )
                self.beta_denominator = self.form_handler.scalar_product(
                    self.difference, self.search_direction
                )
                self.beta = self.beta_numerator / self.beta_denominator

            elif self.cg_method == "DY":
                for i in range(len(self.gradient)):
                    self.difference[i].vector().vec().aypx(
                        0.0,
                        self.gradient[i].vector().vec()
                        - self.gradient_prev[i].vector().vec(),
                    )

                self.beta_numerator = self.form_handler.scalar_product(
                    self.gradient, self.gradient
                )
                self.beta_denominator = self.form_handler.scalar_product(
                    self.search_direction, self.difference
                )
                self.beta = self.beta_numerator / self.beta_denominator

            elif self.cg_method == "HZ":
                for i in range(len(self.gradient)):
                    self.difference[i].vector().vec().aypx(
                        0.0,
                        self.gradient[i].vector().vec()
                        - self.gradient_prev[i].vector().vec(),
                    )

                dy = self.form_handler.scalar_product(
                    self.search_direction, self.difference
                )
                y2 = self.form_handler.scalar_product(self.difference, self.difference)

                for i in range(len(self.gradient)):
                    self.difference[i].vector().vec().axpy(
                        -2 * y2 / dy, self.search_direction[i].vector().vec()
                    )

                self.beta = (
                    self.form_handler.scalar_product(self.difference, self.gradient)
                    / dy
                )
        else:
            self.beta = 0.0

    def compute_search_direction(self) -> None:

        for i in range(len(self.gradient)):
            self.search_direction[i].vector().vec().aypx(
                self.beta, -self.gradient[i].vector().vec()
            )

    def restart(self) -> None:

        if self.cg_periodic_restart:
            if self.memory < self.cg_periodic_its:
                self.memory += 1
            else:
                for i in range(len(self.gradient)):
                    self.search_direction[i].vector().vec().aypx(
                        0.0, -self.gradient[i].vector().vec()
                    )
                self.memory = 0
        if self.cg_relative_restart:
            if (
                abs(self.form_handler.scalar_product(self.gradient, self.gradient_prev))
                / pow(self.gradient_norm, 2)
                >= self.cg_restart_tol
            ):
                for i in range(len(self.gradient)):
                    self.search_direction[i].vector().vec().aypx(
                        0.0, -self.gradient[i].vector().vec()
                    )

    def store_previous_gradient(self) -> None:

        for i in range(len(self.gradient)):
            self.gradient_prev[i].vector().vec().aypx(
                0.0, self.gradient[i].vector().vec()
            )

    def project_ncg_search_direction(self) -> None:

        self.optimization_variable_handler.project_ncg_search_direction(
            self.search_direction
        )
