
import sys
import os
import pytest
from unittest.mock import patch, MagicMock
import datetime
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../../'))
sys.path.insert(0, project_root)

from etlbronze.services.obs_conn import log_observability

@pytest.fixture
def mock_db_connection():
    with patch('etlbronze.services.obs_conn.get_postgres_connection') as mock_get_conn:
        mock_conn = MagicMock()
        mock_cursor = MagicMock()

        mock_get_conn.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        yield mock_conn, mock_cursor

def test_log_observability_success(mock_db_connection):
    mock_conn, mock_cursor = mock_db_connection

    metric_name = 'test_metric'
    start_time = datetime.datetime(2021, 1, 1, 0, 0, 0)
    end_time = datetime.datetime(2021, 1, 1, 0, 1, 0)
    details = {'key': 'value'}
    name_table = 'test_table'

    log_observability(metric_name, start_time, end_time, details, name_table)

    create_table_sql = '''
        CREATE TABLE IF NOT EXISTS modulo8si.observability_g3 (
            id SERIAL PRIMARY KEY,
            metric_name VARCHAR(255),
            start_time BIGINT,
            end_time BIGINT,
            duration INTERVAL,
            details JSON,
            name_table VARCHAR(255)
        )
    '''
    mock_cursor.execute.assert_any_call(create_table_sql)

    insert_sql = '''
        INSERT INTO modulo8si.observability_g3 (metric_name, start_time, end_time, duration, details, name_table)
        VALUES (%s, %s, %s, %s, %s, %s)
    '''
    start_time_unix = int(start_time.timestamp())
    end_time_unix = int(end_time.timestamp())
    duration = datetime.timedelta(seconds=(end_time_unix - start_time_unix))
    details_json = json.dumps(details)

    mock_cursor.execute.assert_any_call(
        insert_sql,
        (metric_name, start_time_unix, end_time_unix, duration, details_json, name_table)
    )

    mock_conn.commit.assert_called_once()
    mock_cursor.close.assert_called_once()
    mock_conn.close.assert_called_once()

def test_log_observability_connection_error():
    with patch('etlbronze.services.obs_conn.get_postgres_connection') as mock_get_conn:
        mock_get_conn.side_effect = Exception("Falha na conexão com o banco de dados")

        metric_name = 'test_metric'
        start_time = datetime.datetime(2021, 1, 1, 0, 0, 0)
        end_time = datetime.datetime(2021, 1, 1, 0, 1, 0)
        details = {'key': 'value'}
        name_table = 'test_table'

        with pytest.raises(Exception) as exc_info:
            log_observability(metric_name, start_time, end_time, details, name_table)

        assert str(exc_info.value) == "Falha na conexão com o banco de dados"
