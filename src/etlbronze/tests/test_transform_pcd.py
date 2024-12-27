import pytest
from unittest.mock import patch
import pandas as pd
import sys
import os
import pytest
from unittest.mock import patch, MagicMock
import datetime
import json
from services.servicesetl.servicetransform.transformpcd import Transform

@pytest.fixture
def sample_data():
    data = {
        'Dt Destino': ['2024-11-28', '2024-11-29', '2024-11-30'],
        'Dt Operacional': ['2024-11-27', '2024-11-28', '2024-11-29'],
        'Dt Origem': ['2024-11-26', '2024-11-27', '2024-11-28'],
        'Fl Alerta': [1, 0, 1],
        'Grupos PCD': ['A', 'B', 'C'],
        'Id Carro': [101, 102, 103],
        'Id Estacao Alerta': [201, 202, 203],
        'Id Estacao Destino': [301, 302, 303],
        'Id Estacao Origem': [401, 402, 403],
        'Id Registro': [501, 502, 503],
        'Tx Descr Linha': ['Linha 1', 'Linha 2', 'Linha 3'],
        'Tx Estacao Destino': ['Estação A', 'Estação B', 'Estação C'],
        'Tx Linha': ['Linha A', 'Linha B', 'Linha C'],
        'Tx Obs': ['Obs1', 'Obs2', 'Obs3'],
        'Tx Porta': [10, 20, 30],
        'Tx Prefixo': ['Prefixo1', 'Prefixo2', 'Prefixo3'],
        'Tx Tipo Pcd': ['Tipo1', 'Tipo2', 'Tipo3'],
        'Tx Trem': ['Trem1', 'Trem2', 'Trem3'],
        'Tx Username Destino': ['UserA', 'UserB', 'UserC'],
        'Tx Username Origem': ['UserX', 'UserY', 'UserZ']
    }
    return pd.DataFrame(data)

@pytest.fixture
def sample_data_with_errors():
    data = {
        'Dt Destino': ['2024-11-28', 'invalid_date', None],
        'Dt Operacional': ['2024-11-27', '2024-11-28', '2024-11-29'],
        'Dt Origem': ['2024-11-26', '2024-11-27', None],
        'Fl Alerta': [1, 0, None],
        'Grupos PCD': ['A', None, 'C'],
        'Id Carro': [101, 102, None],
        'Id Estacao Alerta': [201, None, 203],
        'Id Estacao Destino': [301, 302, None],
        'Id Estacao Origem': [401, 402, 403],
        'Id Registro': [501, None, 503],
        'Tx Porta': [10, 20, None],
    }
    return pd.DataFrame(data)

@pytest.fixture
def transform(sample_data):
    """Fixture para instanciar a classe Transform com dados válidos."""
    data_path = '/path/to/fake_data.parquet'
    name_table = 'test_table'
    
    with patch('pandas.read_parquet') as mock_read_parquet:
        mock_read_parquet.return_value = sample_data
        transform_instance = Transform(data_path, name_table)
        return transform_instance    
    
@pytest.fixture
def transform_with_errors(sample_data_with_errors):
    """Fixture para instanciar a classe Transform com dados inválidos."""
    data_path = '/path/to/pcd_with_errors.parquet'
    name_table = 'test_table_with_errors'
    
    with patch('pandas.read_parquet') as mock_read_parquet:
        mock_read_parquet.return_value = sample_data_with_errors
        transform_instance = Transform(data_path, name_table)
        return transform_instance
    
class BaseTestTransform:
    """Classe base para centralizar os testes da transformação de dados."""

    def assert_data_length(self, data, expected_length):
        """Método auxiliar para verificar o comprimento dos dados transformados."""
        assert len(data) == expected_length, (
            f"O número de viagens transformadas não é o esperado. Encontrado: {len(data)}"
)

class TestTransformDataSuccess(BaseTestTransform):
    def test_transform_data(self, transform):
        """Testa o método de transformação de dados com dados válidos."""
        expected_length = 3  
        viagens_resultado = transform.transform_data()
        self.assert_data_length(viagens_resultado, expected_length)

class TestTransformDataFailure(BaseTestTransform):
    def test_transform_data_failure(self, transform_with_errors):
        """Teste com dados inválidos."""
        expected_transformed = 1  
        viagens_resultado = transform_with_errors.transform_data()
        self.assert_data_length(viagens_resultado, expected_transformed)



