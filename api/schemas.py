from typing import Optional
from pydantic import BaseModel
from api.models.railroad import Railroad


class HealthCheckResponse(BaseModel):
    status: str = "ok"


class OptimizationInput(BaseModel):
    init_date: int
    end_date: int
    code: int
    railroad: Railroad

    class Config:
        schema_extra = {
            "example": {
                "init_date": 1648771200,
                "end_date": 1651276800,
                "code": 255575,
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
        }


class OptimizationOutput(BaseModel):
    code: int
    message: str


class NotFoundError(BaseModel):
    message: Optional[str] = None
