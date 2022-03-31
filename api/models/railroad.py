"""
Railroad model.
"""

import numpy as np
from pydantic.dataclasses import dataclass
from api.models.train_model import TrainModel
from api.models.wagons import WagonsByFleet
from api.models.locomotives import LocomotivesBySeries


@dataclass
class Railroad:
    train_models: list[TrainModel]
    wagons: list[WagonsByFleet]
    locomotives: list[LocomotivesBySeries]

    def train_models_wagons(self):
        wagons = np.array(
            [
                train_model.wagons
                for train_model in self.train_models
            ]
        )

        return wagons

    def train_models_locomotives(self):
        locomotives = np.array(
            [
                train_model.locomotives
                for train_model in self.train_models
            ]
        )

        return locomotives

    def total_wagons(self):
        total = sum(
            wagons_by_fleet.total
            for wagons_by_fleet in self.wagons
        )

        return total

    def total_locomotives(self):
        total = sum(
            locomotives_by_series.total
            for locomotives_by_series in self.locomotives
        )

        return total
