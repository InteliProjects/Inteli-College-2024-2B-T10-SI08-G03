import sys
import os
import pytest
from unittest.mock import patch, MagicMock

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../../'))
sys.path.insert(0, project_root)

from etlbronze.services.create_view import NewView
from etlbronze.Views.intervalo_de_trens import IntervalosTrensEstacoes

@pytest.fixture
def mock_new_view():
    with patch('etlbronze.services.create_view.NewView') as MockNewView:
        mock_instance = MagicMock()
        MockNewView.return_value = mock_instance
        yield mock_instance

def test_create_view_success(mock_new_view, capfd):
    mock_new_view.create_view.side_effect = lambda v, q: print("Creating view...\nView intervalos_estacoes_trens created successfully.")

    intervalos = IntervalosTrensEstacoes()
    intervalos.create_view()

    out, err = capfd.readouterr()
    assert "Creating view..." in out
    assert "View intervalos_estacoes_trens created successfully." in out

def test_create_view_no_error(mock_new_view, capfd):
    mock_new_view.create_view.side_effect = lambda v, q: print("Creating view...\nView intervalos_estacoes_trens created successfully.")

    intervalos = IntervalosTrensEstacoes()
    intervalos.create_view()

    out, err = capfd.readouterr()
    assert "Error creating view:" not in out
