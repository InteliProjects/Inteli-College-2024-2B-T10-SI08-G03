import pytest
from unittest.mock import patch, MagicMock
from etlbronze.Views.viagens_por_linha import ViagensPorLinha

def test_viagens_por_linha_create_view():
    # Patch da classe NewView dentro do módulo viagens_por_linha.py
    with patch('etlbronze.Views.viagens_por_linha.NewView') as MockNewView:
        # Cria uma instância mockada de NewView
        mock_new_view_instance = MockNewView.return_value
        mock_new_view_instance.create_view = MagicMock()

        # Instancia a classe a ser testada
        viagens_por_linha = ViagensPorLinha()
        viagens_por_linha.create_view()

        # Verifica se o método create_view foi chamado exatamente uma vez
        mock_new_view_instance.create_view.assert_called_once()

        # Obtém os argumentos passados na chamada do método mockado
        args, kwargs = mock_new_view_instance.create_view.call_args

        # Verifica os argumentos nomeados
        assert kwargs['view_name'] == "viagens_por_linha"

        # Verifica a presença das palavras-chave esperadas na query
        query = kwargs['query']
        assert "SELECT" in query
        assert "FROM grupo3.working_travels" in query
        assert "GROUP BY" in query
        assert "travel_date" in query
        assert "line" in query
        assert "total_travels" in query
        assert "ORDER BY" in query
        assert "ASC" in query
