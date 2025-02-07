from unittest.mock import MagicMock, patch
import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from services.servicesetl.serviceloading.loading import Loading

@pytest.fixture
def mock_clickhouse_client():
    mock_client = MagicMock()
    mock_client.command.return_value = [("21.8.5.7", "UTC")]  
    mock_client.insert.return_value = None  
    return mock_client

@patch("services.servicesetl.serviceloading.loading.get_client")
@patch("services.servicesetl.serviceloading.loading.time.time", return_value=1732891659) 
def test_load_data_happy_path(mock_time, mock_get_client, mock_clickhouse_client):
    mock_get_client.return_value = mock_clickhouse_client

    loader = Loading(
        clickhouse_host="localhost",
        clickhouse_database="test_db",
        username="user",
        password="password"
    )

    mock_load_data_input = {
        "data": ['{"linha": "A", "passageiros": 120}', '{"linha": "B", "passageiros": 150}'],
        "data_tag": "test_tag",
        "name_table": "working_travels",
    }

    expected_data = pd.DataFrame({
        "data_ingestao": [1732891659, 1732891659],  
        "data_linha": ['{"linha": "A", "passageiros": 120}', '{"linha": "B", "passageiros": 150}'],
        "data_tag": ["test_tag", "test_tag"]
    })


    loader.load_data(
        data=mock_load_data_input["data"],
        data_tag=mock_load_data_input["data_tag"],
        name_table=mock_load_data_input["name_table"]
    )

 
    assert mock_clickhouse_client.insert.call_count == 1  
    args, kwargs = mock_clickhouse_client.insert.call_args  
    inserted_df = args[1]  
    assert_frame_equal(inserted_df, expected_data)  

@patch("services.servicesetl.serviceloading.loading.get_client")
@patch("services.servicesetl.serviceloading.loading.time.time", return_value=1732891659)
def test_load_data_unhappy_path_no_data(mock_time, mock_get_client, mock_clickhouse_client):
    mock_get_client.return_value = mock_clickhouse_client

    loader = Loading(
        clickhouse_host="localhost",
        clickhouse_database="test_db",
        username="user",
        password="password"
    )

  
    loader.load_data(data=[], data_tag="test_tag", name_table="working_travels")

    mock_clickhouse_client.insert.assert_not_called()
