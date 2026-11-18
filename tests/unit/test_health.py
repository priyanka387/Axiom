from axiom_api.main import app
from fastapi.testclient import TestClient


def test_live_health() -> None:
    with TestClient(app) as client:
        response = client.get("/health/live")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
