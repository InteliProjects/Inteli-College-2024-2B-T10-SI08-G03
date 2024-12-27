import os
from dotenv import load_dotenv
from clickhouse_connect import get_client

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class ClickHouseService:
    def __init__(self):
        """
        Inicializa o cliente ClickHouse com os parâmetros do .env.
        """
        self.client = get_client(
            host=os.getenv("CLICKHOUSE_HOST"),
            username=os.getenv("CLICKHOUSE_USERNAME"),
            password=os.getenv("CLICKHOUSE_PASSWORD"),
            database=os.getenv("CLICKHOUSE_DATABASE")
        )

    def execute_query(self, sql):
        """
        Executa uma consulta SQL no banco de dados ClickHouse.
        :param sql: A string SQL a ser executada.
        :return: O resultado da consulta.
        """
        try:
            result = self.client.query(sql)
            return result.result_rows  # Retorna as linhas de resultado da consulta
        except Exception as e:
            raise Exception(f"Erro ao executar consulta: {e}")
