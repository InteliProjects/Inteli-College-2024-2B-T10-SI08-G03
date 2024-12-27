from clickhouse_connect import get_client

class ClickHouseConnection:
    """
    Classe para gerenciar a conexão com ClickHouse.
    """
    def __init__(self, host: str = "clickhouse-server", database: str = "default", username: str = "default", password: str = ""):
        self.client = get_client(
            host=host,
            port=8123,
            database=database,
            username=username,
            password=password
        )

    def execute_query(self, query):
        """
        Executa uma consulta SQL no banco ClickHouse.
        """
        return self.client.query(query).result_rows
