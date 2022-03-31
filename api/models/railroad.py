"""
Railroad model.
"""

from pydantic.dataclasses import dataclass
from api.models.train_model import TrainModel
from api.models.wagons import WagonsByFleet
from api.models.locomotives import LocomotivesBySeries


@dataclass
class Railroad:
    train_models: list[TrainModel]
    wagons: list[WagonsByFleet]
    locomotives: list[LocomotivesBySeries]
