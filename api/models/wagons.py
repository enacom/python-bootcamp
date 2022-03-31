"""
Railroad wagons availability by fleet.
"""

from pydantic.dataclasses import dataclass


@dataclass(frozen=True, order=True)
class WagonsByFleet:
    fleet: str
    fleet_name: str
    total: int


@dataclass(frozen=True, order=True)
class Wagons:
    wagons_by_fleets: list[WagonsByFleet]
