import pytest
from flask import Flask
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from API.routes.health import health_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(health_bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert "status" in data
    assert data["status"] == "healthy"
