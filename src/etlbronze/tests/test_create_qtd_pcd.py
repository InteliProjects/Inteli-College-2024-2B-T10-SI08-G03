

import sys
import os
import pytest
from unittest.mock import patch, MagicMock


current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../../'))
sys.path.insert(0, project_root)

    
from etlbronze.services.create_view import NewView

@pytest.fixture
def mock_get_client():
        
    with patch('etlbronze.services.create_view.get_client') as mock_client:
        yield mock_client

def test_new_view_initialization(mock_get_client):
    
    clickhouse_host = "srv613520.hstgr.cloud"
    clickhouse_database = "grupo3"
    username = "admin"
    password = "admin123"
    
    
    new_view = NewView(
        clickhouse_host=clickhouse_host,
        clickhouse_database=clickhouse_database,
        username=username,
        password=password
    )
    
    
    mock_get_client.assert_called_once_with(
        host=clickhouse_host,
        port=8123,
        database=clickhouse_database,
        username=username,
        password=password
    )
    
def test_create_view_success(mock_get_client):
    
    mock_client_instance = MagicMock()
    mock_get_client.return_value = mock_client_instance
    
    
    new_view = NewView(
        clickhouse_host="srv613520.hstgr.cloud",
        clickhouse_database="grupo3",
        username="admin",
        password="admin123"
    )
    
    
    view_name = "qtd_pcd_dia"
    query = """
        SELECT
            toDate(JSONExtractFloat(data_linha, 'dt_origin')) AS travel_date,
            JSONExtractInt(data_linha, 'alert_station_id') AS station_id,
            COUNT(*) AS total_pcd
        FROM grupo3.working_travels
        WHERE
            JSONExtractString(data_linha, 'pcd_type') != ''
        GROUP BY
            travel_date,
            station_id
        ORDER BY
            travel_date ASC,
            station_id ASC;
            """
    
   
    new_view.create_view(view_name, query)
    
   
    expected_command = f"CREATE VIEW IF NOT EXISTS grupo3.{view_name} AS {query}"
    mock_client_instance.command.assert_called_once_with(expected_command)

def test_create_view_exception(mock_get_client, capfd):
   
    mock_client_instance = MagicMock()
    mock_client_instance.command.side_effect = Exception("Erro ao criar view")
    mock_get_client.return_value = mock_client_instance
    
    
    new_view = NewView(
        clickhouse_host="srv613520.hstgr.cloud",
        clickhouse_database="grupo3",
        username="admin",
        password="admin123"
    )
    
    
    view_name = "qtd_pcd_dia"
    query = """
        SELECT
            toDate(JSONExtractFloat(data_linha, 'dt_origin')) AS travel_date,
            JSONExtractInt(data_linha, 'alert_station_id') AS station_id,
            COUNT(*) AS total_pcd
        FROM grupo3.working_travels
        WHERE
            JSONExtractString(data_linha, 'pcd_type') != ''
        GROUP BY
            travel_date,
            station_id
        ORDER BY
            travel_date ASC,
            station_id ASC;
            """
    
    
    new_view.create_view(view_name, query)
    
    
    out, err = capfd.readouterr()
    
    
    assert "Creating view..." in out
    assert "Error creating view: Erro ao criar view" in out
