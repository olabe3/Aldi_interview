from fastapi import FastAPI
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_config_lifecycle():
    # POST
    response = client.post("/config", json={"name": "foo", "value": "bar"})
    assert response.status_code == 200
    # GET
    response = client.get("/config/foo")
    assert response.json()["value"] == "bar"
    # DELETE
    response = client.delete("/config/foo")
    assert response.json() == {"deleted": True}