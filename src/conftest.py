import sys
import os

def pytest_configure(config):
    """
    Configura o sys.path dinamicamente baseado no diretório do pacote de teste.
    """
    # Obter o caminho do diretório atual de teste
    current_test_path = os.getcwd()

    # Verifica se o teste está sendo executado em API ou etlbronze
    if "API/tests" in current_test_path:
        root_path = os.path.abspath(os.path.join(current_test_path, ".."))
        print(f"Configurando o root para API: {root_path}")
    elif "etlbronze/tests" in current_test_path:
        root_path = os.path.abspath(os.path.join(current_test_path, ".."))
        print(f"Configurando o root para etlbronze: {root_path}")
    else:
        root_path = os.path.abspath(os.getcwd())
        print(f"Usando root padrão: {root_path}")

    # Adicionar o root_path ao sys.path
    if root_path not in sys.path:
        sys.path.insert(0, root_path)