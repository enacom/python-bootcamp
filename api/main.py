"""
ENACOM Python bootcamp

API (interface de programação de aplicações)
para resolução de problemas de otimização.
"""
from typing import Union
from fastapi import FastAPI
from http import HTTPStatus
from api.schemas import (
    HealthCheckResponse, OptimizationInput, NotFoundError, OptimizationOutput
)
from api.optimization.problem import solve


api = FastAPI(
    title='ENACOM Python bootcamp API',
    version='0.1.1',
    description=(
        'API (Interface de programação de aplicações)'
        'para resolução de problemas de otimização.\n'
    ),
)


@api.get(
    '/healthcheck',
    tags=['healthcheck'],
    summary='Integridade do sistema',
    description='Verifica se o servidor da API está ativo',
    response_model=HealthCheckResponse
)
def healthcheck():
    message = HealthCheckResponse()

    return message


@api.post(
    '/results/{code}',
    summary='Resultado da otimização por código',
    response_model=OptimizationOutput,
    responses={
        HTTPStatus.NOT_FOUND.value: {
            'description': 'Resultado da otimização não encontrado',
            'model': NotFoundError
        }
    }
)
def post_results_code(code: int) -> Union[OptimizationOutput, NotFoundError]:
    pass


@api.post(
    '/solve',
    summary='Resolver o problema de otimização',
    responses={
        HTTPStatus.NOT_FOUND.value: {
            'description': 'Otimização não resolvida',
            'model': NotFoundError
            }
        }
)
def post_solve(
    optimization_input: OptimizationInput
):
    """
    Resolver problema de otimização
    """
    solve(
        optimization_input=optimization_input
    )

    response = {"message": "Problema recebido."}

    return response
