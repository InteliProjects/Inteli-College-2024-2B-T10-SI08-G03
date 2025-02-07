import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
import os


os.environ["API_TOKEN"] = "test_token"

with patch('API.services.clickhouse_service.ClickHouseService') as MockService:
    mock_service = MagicMock()
    mock_service.execute_query.return_value = []
    MockService.return_value = mock_service
    from API.routes.line_routes import api_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    
    app.register_blueprint(api_bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_resposta_vazia(client):
    response = client.get("/api/duracao_viagens/L1", headers={"Authorization": "Bearer test_token"})
    assert response.status_code == 200  

def test_sem_token(client):
    response = client.get("/api/duracao_viagens/L1")
    assert response.status_code == 401
    error_data = response.get_json()
    assert "error" in error_data
    assert "Token inválido ou ausente" in error_data["error"]

def test_viagens_dia_semana_resposta_vazia(client):
    response = client.get("/api/viagens_dia_semana/L1", headers={"Authorization": "Bearer test_token"})
    assert response.status_code == 200
    assert response.get_json() == {"data": []}

def test_viagens_dia_semana_erro_banco(client):
    with patch("API.routes.line_routes.ClickHouseService.execute_query", side_effect=Exception("Database Error")):
        response = client.get("/api/viagens_dia_semana/L1", headers={"Authorization": "Bearer test_token"})
        assert response.status_code == 500
        error_data = response.get_json()
        assert "error" in error_data
        assert "Database Error" in error_data["error"]

def test_quantidade_viagens_origem_resposta_vazia(client):
    response = client.get("/api/quantidade_viagens_origem/L1", headers={"Authorization": "Bearer test_token"})
    assert response.status_code == 200
    assert response.get_json() == {"data": []}

def test_verificar_token_invalido(client):
    response = client.get("/api/duracao_viagens/L1", headers={"Authorization": "Bearer wrong_token"})
    assert response.status_code == 401
    error_data = response.get_json()
    assert "error" in error_data
    assert "Token inválido ou ausente" in error_data["error"]

