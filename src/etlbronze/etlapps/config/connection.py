import psycopg2
from psycopg2.extras import execute_values

def get_db_connection():
    """
    Função para estabelecer uma conexão com o banco de dados PostgreSQL.
    """
    conn = psycopg2.connect(
        host="dpg-cs2rppbv2p9s738nq950-a.oregon-postgres.render.com",  # Endereço do servidor PostgreSQL
        database="backend_ugaz",  # Nome do banco de dados
        user="backend_ugaz_user",  # Usuário do PostgreSQL
        password="87KlrSzD5GQ0M8KBs5SaJ0bJgGj5112g"  # Senha do usuário
    )
    return conn