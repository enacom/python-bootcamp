"""
Railroad locomotives availability by series.
"""

from pydantic.dataclasses import dataclass


@dataclass(frozen=True, order=True)
class LocomotivesBySeries:
    series: str
    total: int
