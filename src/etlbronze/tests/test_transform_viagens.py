import pytest
from unittest.mock import patch
from services.servicesetl.servicetransform.transformviagens import Transform
import pandas as pd


# Fixtures de dados
@pytest.fixture
def sample_data():
    """Fixture para dados válidos para o caso de sucesso."""
    data = {
        'DT_OPERACIONAL': [1609459200, 1609545600],
        'ID_LINHA': [1, 2],
        'TX_DESCR_LINHA': ['Linha A', 'Linha B'],
        'TX_COR_LINHA': ['Vermelho', 'Azul'],
        'NR_ORDEM': [1, 2],
        'TX_PREFIXO': ['P1', 'P2'],
        'DT_INI_VIAGEM': [1609459200, 1609545600],
        'DT_FIM_VIAGEM': [1609462800, 1609549200],
        'NR_DURACAO': [3600, 3600],
        'ID_ORIGEM': [100, 200],
        'ID_DESTINO': [101, 201],
        'TX_ORIGEM': ['Origem A', 'Origem B'],
        'TX_DESTINO': ['Destino A', 'Destino B'],
    }
    return pd.DataFrame(data)

@pytest.fixture
def sample_data_with_errors():
    """Fixture para dados inválidos para o caso de falha."""
    data = {
        'DT_OPERACIONAL': [1609459200, 'invalid_date'],
        'ID_LINHA': [1, 'not_a_number'],
        'TX_DESCR_LINHA': ['Linha A', None],
        'TX_COR_LINHA': ['Vermelho', 'Azul'],
        'NR_ORDEM': [1, None],
        'TX_PREFIXO': ['P1', 'P2'],
        'DT_INI_VIAGEM': [1609459200, None],
        'DT_FIM_VIAGEM': [1609462800, None],
        'NR_DURACAO': [3600, -100],
        'ID_ORIGEM': [100, 200],
        'ID_DESTINO': [101, 201],
        'TX_ORIGEM': ['Origem A', 'Origem B'],
        'TX_DESTINO': ['Destino A', 'Destino B'],
    }
    return pd.DataFrame(data)

@pytest.fixture
def transform(sample_data):
    """Fixture para instanciar a classe Transform com dados válidos."""
    data_path = '/path/to/viagens.parquet'
    name_table = 'test_table'
    
    # Mock para ler o arquivo Parquet
    with patch('pandas.read_parquet') as mock_read_parquet:
        mock_read_parquet.return_value = sample_data
        transform_instance = Transform(data_path, name_table)
        return transform_instance

@pytest.fixture
def transform_with_errors(sample_data_with_errors):
    """Fixture para instanciar a classe Transform com dados inválidos."""
    data_path = '/path/to/viagens_with_errors.parquet'
    name_table = 'test_table_with_errors'
    
    # Mock para ler o arquivo Parquet com dados inválidos
    with patch('pandas.read_parquet') as mock_read_parquet:
        mock_read_parquet.return_value = sample_data_with_errors
        transform_instance = Transform(data_path, name_table)
        return transform_instance

# Classe base para os testes
class BaseTestTransform:
    """Classe base para centralizar os testes da transformação de dados."""

    def assert_data_length(self, data, expected_length):
        """Método auxiliar para verificar o comprimento dos dados transformados."""
        assert len(data) == expected_length, (
            f"O número de viagens transformadas não é o esperado. Encontrado: {len(data)}"
        )

# Classe de teste para o caso de sucesso
class TestTransformDataSuccess(BaseTestTransform):
    """Testes para a transformação de dados válidos."""

    def test_transform_data(self, transform):
        """Testa o método de transformação de dados com dados válidos."""
        # Arrange
        expected_length = 2  # Temos 2 linhas na fixture de dados
        
        # Act
        viagens_resultado = transform.transform_data()

        # Assert
        self.assert_data_length(viagens_resultado, expected_length)

# Classe de teste para o caso de falha
class TestTransformDataFailure(BaseTestTransform):
    """Testes para a transformação de dados com erros."""

    def test_transform_data_failure(self, transform_with_errors):
        """Testa o método de transformação com dados inválidos."""
        # Act
        viagens_resultado = transform_with_errors.transform_data()
        
        # Filtrar registros válidos pelo conteúdo
        registros_validos = [v for v in viagens_resultado if '"NR_DURACAO": 3600' in v]
        
        # Assert
        expected_transformed = 1  # Apenas um registro é válido
        assert len(registros_validos) == expected_transformed, (
            f"Registros válidos não são os esperados. Encontrados: {len(registros_validos)}"
        )

