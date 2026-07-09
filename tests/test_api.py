"""Basic tests for MSP Dashboard API."""
from fastapi.testclient import TestClient


def test_health_endpoint():
    """Test /health returns ok."""
    from api.app import app
    client = TestClient(app)
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_ingest_service_login(db_session):
    """Test event ingestion creates service and staff records."""
    from api.app import app
    client = TestClient(app)
    payload = {
        "staff_email": "tech@example.com",
        "service_name": "email",
        "source_ip": "10.0.0.1",
    }
    resp = client.post("/ingest/service-login", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert "event_id" in data


def test_list_events(db_session):
    """Test /admin/events returns ingested events."""
    from api.app import app
    client = TestClient(app)
    # Ingest first
    client.post("/ingest/service-login", json={
        "staff_email": "tech@example.com",
        "service_name": "email",
        "source_ip": "10.0.0.1",
    })
    resp = client.get("/admin/events?limit=10")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    if data:
        assert "service" in data[0]
        assert "staff_name" in data[0]