import pytest
import pandas as pd
import os
import sys
from unittest.mock import patch

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../../'))
sys.path.insert(0, project_root)

from etlbronze.services.servicesetl.servicetransform.transformintervalos import Transform


# Fixture para dados válidos
@pytest.fixture
def sample_data():
    data = {
        "DT_HORA_MINUTO": [pd.Timestamp("2024-11-01 10:00:00"), pd.Timestamp("2024-11-01 12:00:00")],
        "ID_DT_HORA_MINUTO": [1, 2],
        "HORA_INI": [pd.Timestamp("2024-11-01 10:00:00"), pd.Timestamp("2024-11-01 12:00:00")],
        "HORA_FIM": [pd.Timestamp("2024-11-01 11:00:00"), pd.Timestamp("2024-11-01 13:00:00")],
        "DURATION_MINUTES": [60.0, 60.0]
    }
    return pd.DataFrame(data)


# Fixture para dados com erros
@pytest.fixture
def sample_data_with_errors():
    data = {
        "DT_HORA_MINUTO": [pd.Timestamp("2024-11-01 10:00:00"), None],
        "ID_DT_HORA_MINUTO": [1, "invalid_id"],
        "HORA_INI": [pd.Timestamp("2024-11-01 10:00:00"), None],
        "HORA_FIM": [pd.Timestamp("2024-11-01 11:00:00"), pd.Timestamp("2024-11-01 13:00:00")],
        "DURATION_MINUTES": [60.0, "not_a_number"]
    }
    return pd.DataFrame(data)


# Fixture para instância de Transform com dados válidos
@pytest.fixture
def transform(sample_data):
    data_path = '/path/to/intervalos.parquet'
    name_table = 'test_table'

    with patch('pandas.read_parquet') as mock_read_parquet:
        mock_read_parquet.return_value = sample_data
        transform_instance = Transform(data_path, name_table)
        return transform_instance


# Fixture para instância de Transform com dados inválidos
@pytest.fixture
def transform_with_errors(sample_data_with_errors):
    data_path = '/path/to/intervalos_with_errors.parquet'
    name_table = 'test_table_with_errors'

    with patch('pandas.read_parquet') as mock_read_parquet:
        mock_read_parquet.return_value = sample_data_with_errors
        transform_instance = Transform(data_path, name_table)
        return transform_instance


# Classe base para testes
class BaseTestTransform:
    def assert_data_length(self, data, expected_length):
        assert len(data) == expected_length, (
            f"O número de intervalos transformados não é o esperado. Encontrado: {len(data)}")


# Classe de teste para o caso de sucesso
class TestTransformDataSuccess(BaseTestTransform):
    """Testes para a transformação de dados válidos."""

    def test_transform_data(self, transform):
        """Testa o método de transformação de dados com dados válidos."""
        # Arrange
        expected_length = 2

        # Act
        intervals_result = transform.transform_data()

        # Assert
        self.assert_data_length(intervals_result, expected_length)


# Classe de teste para o caso de falha
class TestTransformDataFailure(BaseTestTransform):
    """Testes para a transformação de dados com erros."""

    def test_transform_data_failure(self, transform_with_errors):
        """Testa o método de transformação com dados inválidos."""
        # Arrange
        expected_transformed = 1 

        # Act
        intervals_result = transform_with_errors.transform_data()

        # Assert
        self.assert_data_length(intervals_result, expected_transformed)
