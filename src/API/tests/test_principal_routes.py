import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
import os

os.environ["API_TOKEN"] = "test_token"

with patch('API.services.clickhouse_service.ClickHouseService') as MockService:
    mock_service = MagicMock()
    mock_service.execute_query.return_value = []
    MockService.return_value = mock_service
    from API.routes.principal_routes import api_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(api_bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.mark.parametrize("endpoint", [
    "/api/qtd_viagens_por_linha",
    "/api/duracao_media",
    "/api/duracao_real_programada",
    "/api/taxa_atraso",
    "/api/viagens_por_dia_mes",
    "/api/qtd_viagens_semana_linha",
    "/api/alertas_pcd_por_linha",
    "/api/qtd_pcd_semana_linha",
    "/api/qtd_pcd_por_dia"
])
def test_resposta_vazia(client, endpoint):
    """Testa resposta vazia para todos os endpoints."""
    mock_service.execute_query.return_value = []
    response = client.get(endpoint, headers={"Authorization": "Bearer test_token"})
    assert response.status_code == 200
    data = response.get_json()["data"]
    assert len(data) == 0

@pytest.mark.parametrize("endpoint", [
    "/api/qtd_viagens_por_linha",
    "/api/duracao_media",
    "/api/duracao_real_programada",
    "/api/taxa_atraso",
    "/api/viagens_por_dia_mes",
    "/api/qtd_viagens_semana_linha",
    "/api/alertas_pcd_por_linha",
    "/api/qtd_pcd_semana_linha",
    "/api/qtd_pcd_por_dia"
])
def test_sem_token(client, endpoint):
    """Testa erro de autenticação para todos os endpoints."""
    response = client.get(endpoint)
    assert response.status_code == 401
    error_data = response.get_json()
    assert "error" in error_data
    assert "Token inválido ou ausente" in error_data["error"]

def test_qtd_viagens_por_linha_com_dados(client):
    """Testa o endpoint /api/qtd_viagens_por_linha com dados simulados."""
    mock_service.execute_query.return_value = [("L1", 50), ("L2", 75)]
    response = client.get("/api/qtd_viagens_por_linha", headers={"Authorization": "Bearer test_token"})
    assert response.status_code == 200
    data = response.get_json()["data"]
    assert len(data) == 2
    assert data[0] == {"line": "L1", "total_travels": 50}
    assert data[1] == {"line": "L2", "total_travels": 75}

def test_duracao_media_com_dados(client):
    """Testa o endpoint /api/duracao_media com dados simulados."""
    mock_service.execute_query.return_value = [
        ("2024-01-01", "L1", 120),
        ("2024-01-02", "L2", 150)
    ]
    response = client.get("/api/duracao_media", headers={"Authorization": "Bearer test_token"})
    assert response.status_code == 200
    data = response.get_json()["data"]
    assert len(data) == 2
    assert data[0] == {"data_operacional": "2024-01-01", "linha": "L1", "duracao_media": 120}
    assert data[1] == {"data_operacional": "2024-01-02", "linha": "L2", "duracao_media": 150}

def test_erro_no_banco(client):
    """Testa erro no banco de dados para o endpoint /api/qtd_viagens_por_linha."""
    mock_service.execute_query.side_effect = Exception("Erro no banco de dados")
    response = client.get("/api/qtd_viagens_por_linha", headers={"Authorization": "Bearer test_token"})
    assert response.status_code == 500
    error_data = response.get_json()
    assert "error" in error_data
    assert "Erro no banco de dados" in error_data["error"]
