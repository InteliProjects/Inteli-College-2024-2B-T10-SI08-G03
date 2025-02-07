import pytest
from unittest.mock import patch, MagicMock
from etlbronze.Views.IntervalosEstacoes import IntervalosEstacoes

def test_intervalos_estacoes_create_view():
    with patch('etlbronze.Views.IntervalosEstacoes.NewView') as MockNewView:
        mock_new_view_instance = MockNewView.return_value
        mock_new_view_instance.create_view = MagicMock()

        intervalos_estacoes = IntervalosEstacoes()
        intervalos_estacoes.create_view()

        mock_new_view_instance.create_view.assert_called_once()

        args, kwargs = mock_new_view_instance.create_view.call_args

        assert args[0] == "station_line_day_intervals"

        query = args[1]

        assert "SELECT" in query
        assert "FROM" in query
        assert "grupo5.data_ingestion" in query
        assert "station_id" in query
        assert "dia" in query
        assert "media_intervalo" in query
        assert "AVG(" in query
        assert "GROUP BY" in query
