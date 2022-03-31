"""
Tests for API client.
"""

from fastapi.testclient import TestClient
from http import HTTPStatus
from api.main import api


def test_healthcheck_status_code_ok():
    client = TestClient(api)
    response = client.get("/healthcheck")

    assert response.status_code == HTTPStatus.OK


def test_healthcheck_content_json():
    client = TestClient(api)
    response = client.get("/healthcheck")

    assert response.headers["Content-Type"] == "application/json"


def test_healthcheck_response_message_status_ok():
    client = TestClient(api)
    response = client.get("/healthcheck")
    message = {
        "status": "ok"
    }

    assert response.json() == message


def test_post_solve_status_code_ok():
    client = TestClient(api)
    response = client.post(
        "/solve",
        json={
            "code": 7654321,
            "railroad": {
                "train_models": [
                    {
                        "wagons": 50
                    },
                    {
                        "wagons": 75
                    }
                ],
                "fleets": [
                    {
                        "wagons": 1500
                    }
                ]

            }
        }
    )

    assert response.status_code == HTTPStatus.OK


def test_post_results_status_code_ok():
    client = TestClient(api)
    response = client.post(
        "/results/{7654321}",
        json={
            "code": 7654321,
            "railroad": {
                "train_models": [
                    {
                        "wagons": 50
                    },
                    {
                        "wagons": 75
                    }
                ],
                "fleets": [
                    {
                        "wagons": 1500
                    }
                ]

            }
        }
    )

    assert response.status_code == HTTPStatus.OK
