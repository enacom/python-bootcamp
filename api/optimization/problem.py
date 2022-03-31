"""
Optimization for train model allocation.
"""
import numpy as np
from api.schemas import OptimizationInput, OptimizationOutput
from science_optimization.builder import OptimizationProblem
from science_optimization.problems import MIP
from science_optimization.solvers import Optimizer
from science_optimization.algorithms.linear_programming import Glop


"""
## Problema
Encontrar a alocação ótima dos modelos de trens.

Objetivo: maximizar a quantidade de vagões em trem.
Restrições: disponibilidade de vagões e locomotivas.

\begin{align}
\minimize_x & -\sum_{i}x_i w_i\\
\text{subject to}
&\sum_{i}x_i l_i \leq L\\
&\sum_{i}x_i w_i \leq W\\
&x_i \in \mathbb{N}
\end{align}
onde:
* $i$ é o índice do modelo de trem;
* $w_i$ é a quantidade de vagões do modelo de trem $i$;
* $l_i$ é a quantidade de locos do modelo de trem $i$;
* $W$  é a disponiblilidade de vagões;
* $L$ é a disponiblilidade de locomotivas;
* $x_i$ é a quantidade de trens alocados por modelo.
"""


def build_allocation_problem(
    wagons: np.ndarray,
    locomotives: np.ndarray,
    total_wagons: int,
    total_locomotives: int,
    verbose: bool = True
) -> OptimizationProblem:
    """
    Build a allocation optimization problem.

    Args:
        wagons (np.ndarray): Wagons for each train model.
        locomotives (np.ndarray): Locomotives for each train model.
        total_wagons (int): Total of available wagons.
        total_locomotives (int): Total of available locomotives.
        verbose (bool, optional): Show problem informations. Defaults to True.

    Raises:
        ValueError: Inconsistent problem when total of models is diffents
        for locomotives and wagons. Also inconsistent problem when or
        total of available wagons or locomotives are negatives.

    Returns:
        OptimizationProblem: Structured optimization problem.
    """
    # check consistency
    if (
        len(locomotives) != len(wagons)
        or total_wagons < 0
        or total_locomotives < 0
    ):
        raise ValueError(
            f"Inconsistent problem!\n{total_locomotives=}, {total_wagons=}\n"
            f"{len(locomotives)=}, {len(wagons)=}"
        )

    total_models = len(locomotives)

    # build objective parameters
    objective = -1. * wagons.reshape(-1, 1)

    # build wagon and locomotive constraint
    model = np.column_stack([wagons, locomotives]).T
    total = np.array([total_wagons, total_locomotives]).reshape(-1, 1)

    # build variables bounds and type
    bounds = np.tile(np.array([[0, np.inf]]), reps=(total_models, 1))
    types = ['d'] * total_models  # discrete variable

    # problem
    builder = MIP(
        c=objective,
        A=model,
        b=total,
        x_bounds=bounds,
        x_type=types
    )

    problem = OptimizationProblem(builder)

    # log
    if verbose:
        problem.info()

    return problem


def optimize_allocation(
    problem: OptimizationProblem
) -> tuple[np.ndarray, np.ndarray]:
    """
    Solver a optimization allocation problem.

    Args:
        problem (OptimizationProblem): Structured optimization problem.

    Returns:
        tuple[ndarray, ndarray]: train_models end allocation.
    """
    # builder optimization
    optimizer = Optimizer(
        opt_problem=problem,
        algorithm=Glop()
    )

    results = optimizer.optimize()

    models = problem.constraints.A()
    limits = problem.constraints.b()
    allocation = results.x
    allocated_wagons = -1 * results.fx
    allocated_locomotives = models[1, :] @ allocation

    # print results
    for i in range(models.shape[1]):
        print(
            f"number of trains using {models[0, i]} wagons"
            f" and {models[1, i]} locomotives: {allocation[i][0]}"
        )

    print(
        f"number of used wagons: {allocated_wagons[0]}"
        f" of {limits[0][0]}"
    )

    print(
        f"number of used locomotives: {allocated_locomotives[0]}"
        f" of {limits[1][0]}"
    )

    return models, allocation


def solve(
    optimization_input: OptimizationInput
):
    """
    Build and optimize allocation problem.

    Args:
        optimization_input (OptimizationInput): Allocation problem input data.
    """
    # parameters
    wagons = optimization_input.railroad.train_models_wagons()
    locomotives = optimization_input.railroad.train_models_locomotives()
    total_wagons = optimization_input.railroad.total_wagons()
    total_locomotives = optimization_input.railroad.total_locomotives()

    # build optimization problem
    problem = build_allocation_problem(
        wagons=wagons,
        locomotives=locomotives,
        total_wagons=total_wagons,
        total_locomotives=total_locomotives
    )

    models, allocation = optimize_allocation(problem=problem)

    # TODO: Salvar os resultados:
    # models e allocation na estrutura do OptimizationOutput.
    # Esse dados de saída tem que ficar disponível para a
    # rota: '/results/{code}'
    # Faça as modificações que forem necessárias.
