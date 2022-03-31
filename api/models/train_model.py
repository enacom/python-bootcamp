"""
Railroad train model.
"""

from pydantic.dataclasses import dataclass


@dataclass
class TrainModel:
    series: str
    locomotives: int
    wagons: int


@dataclass
class TrainModels:
    models: list[TrainModel]
