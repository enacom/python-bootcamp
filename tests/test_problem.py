"""
Tests for optimization problem.
"""

import pytest
import numpy as np
from science_optimization.builder import OptimizationProblem
from science_optimization.problems import MIP
from api.optimization.problem import (
    build_allocation_problem,
    optimize_allocation,
    solve,
)
from api.schemas import OptimizationInput, OptimizationOutput
from api.models.optimization_results import OptimizationResults
from api.models.railroad import Railroad
from api.models.wagons import WagonsByFleet
from api.models.locomotives import LocomotivesBySeries
from api.models.train_model import TrainModelUsage


def test_build_allocation_problem_ok():

    # Objetivo: maximizar a quantidade de vagões em trem
    objective = np.array([-43, -56]).reshape(-1, 1)

    model = np.array(
        [
            # vagões dos modelos de trem
            [
                43, 56,
            ],
            # locomotivas dos modelos de trem
            [
                3, 4
            ]
        ]
    )

    # Total vagões e total de locomotivas
    total = np.array([615, 22]).reshape(-1, 1)

    # Domínio das variáveis, números naturais
    bounds = np.array(
        [
            [0., np.inf],
            [0., np.inf]
        ]
    )

    # Variáveis discretas
    types = ['d', 'd']

    builder = MIP(
        c=objective,
        A=model,
        b=total,
        x_bounds=bounds,
        x_type=types
    )

    problem = OptimizationProblem(builder)

    wagons = np.array([43, 56])
    locomotives = np.array([3, 4])
    total_wagons = 615
    total_locomotives = 22

    result = build_allocation_problem(
        wagons=wagons,
        locomotives=locomotives,
        total_wagons=total_wagons,
        total_locomotives=total_locomotives,
    )

    assert result.info() == problem.info()


def test_build_allocation_problem_raise_value_error():
    message = (
        "Inconsistent problem!\ntotal_locomotives=22, total_wagons=615\n"
        "len(locomotives)=2, len(wagons)=1"
    )

    wagons = np.array([43])
    locomotives = np.array([3, 4])
    total_wagons = 615
    total_locomotives = 22

    with pytest.raises(ValueError) as error:

        _ = build_allocation_problem(
            wagons=wagons,
            locomotives=locomotives,
            total_wagons=total_wagons,
            total_locomotives=total_locomotives,
        )

    assert str(error.value) == message


def test_solve_optimization_output_ok():

    model0_usage = {
        "usage": 6,
        "train_model": {
            "series": "LC80",
            "locomotives": 3,
            "wagons": 43
        }
    }

    model1_usage = {
        "usage": 1,
        "train_model": {
            "series": "LC80",
            "locomotives": 4,
            "wagons": 56
        }
    }

    optimization_output = OptimizationOutput(
        code=144464,
        message="",
        results=OptimizationResults(
            wagons=[
                WagonsByFleet(
                    fleet=15800,
                    fleet_name="Frota ENACOM",
                    total=314,
                )
            ],
            locomotives=[
                LocomotivesBySeries(
                    series="LC80",
                    total=22
                )
            ],
            train_models_usage=[
                TrainModelUsage(**model0_usage),
                TrainModelUsage(**model1_usage)
            ]
        )
    )

    input_data = {
        "init_date": 1646092800,
        "end_date": 1648684800,
        "code": 144464,
        "railroad": {
            "train_models": [
                {
                    "series": "LC80",
                    "locomotives": 3,
                    "wagons": 43
                },
                {
                    "series": "LC80",
                    "locomotives": 4,
                    "wagons": 56
                }
            ],
            "wagons": [
                {
                    "fleet": "15800",
                    "fleet_name": "Frota ENACOM",
                    "total": 615
                }
            ],
            "locomotives": [
                {
                    "series": "LC80",
                    "total": 22
                }
            ]
        }
    }

    optimization_input = OptimizationInput(**input_data)

    results = solve(optimization_input)

    assert results == optimization_output
