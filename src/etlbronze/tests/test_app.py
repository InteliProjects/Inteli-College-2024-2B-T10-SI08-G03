# etlbronze/tests/test_app.py

import sys
import os
import pytest
from unittest.mock import Mock, patch
from flask import Flask


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

@pytest.fixture(scope='module')
def app_mocked():
    """
    Fixture que mocka 'etlbronze.app.routes' antes de importar 'etlbronze.app'
    """
    with patch('etlbronze.app.routes', Mock()):
        from etlbronze.app import app
        yield app

@pytest.fixture
def client(app_mocked):
    """
    Fixture que cria um cliente de teste do Flask
    """
    app_mocked.config['TESTING'] = True
    with app_mocked.test_client() as client:
        yield client

def test_app_initialization(app_mocked):
    """Verifica se o aplicativo Flask foi inicializado corretamente."""
    assert app_mocked is not None

def test_app_is_flask_instance(app_mocked):
    """Verifica se o aplicativo é uma instância do Flask."""
    assert isinstance(app_mocked, Flask)


