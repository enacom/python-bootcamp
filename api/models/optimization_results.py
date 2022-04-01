"""
Optimization problem results model.
"""
from pydantic import Field
from pydantic.dataclasses import dataclass
from api.models.train_model import TrainModelUsage
from api.models.wagons import WagonsByFleet
from api.models.locomotives import LocomotivesBySeries


@dataclass
class OptimizationResults:
    wagons: list[WagonsByFleet] = Field(default_factory=list)
    locomotives: list[LocomotivesBySeries] = Field(default_factory=list)
    train_models_usage: list[TrainModelUsage] = Field(default_factory=list)
