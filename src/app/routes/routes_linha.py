import os
from flask import Blueprint, request, jsonify
from services.clickhouse import ClickHouseConnection
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
CLICKHOUSE_HOST = os.getenv("CLICKHOUSE_HOST")
CLICKHOUSE_DATABASE = os.getenv("CLICKHOUSE_DATABASE")
CLICKHOUSE_USERNAME = os.getenv("CLICKHOUSE_USERNAME")
CLICKHOUSE_PASSWORD = os.getenv("CLICKHOUSE_PASSWORD")

clickhouse = ClickHouseConnection(
    host=CLICKHOUSE_HOST,
    database=CLICKHOUSE_DATABASE,
    username=CLICKHOUSE_USERNAME,
    password=CLICKHOUSE_PASSWORD
)

api_bp = Blueprint("api_linha", __name__)

def verificar_token():
    token = request.headers.get("Authorization")
    if not token or token != f"Bearer {API_TOKEN}":
        return jsonify({"error": "Token inválido ou ausente"}), 401
    return None

@api_bp.route("/api/duracao_viagens/<linha>", methods=["GET"])
def duracao_viagens(linha):
    """Endpoint para obter a duração real, programada e diferença das viagens para uma linha específica."""
    auth_error = verificar_token()
    if auth_error:
        return auth_error

    try:
        sql = f"""
        SELECT
            linha,
            id_viagem,
            duracao_real,
            duracao_programada,
            diferenca
        FROM grupo3.view_duracao_viagens
        WHERE linha = '{linha}'
        ORDER BY id_viagem ASC
        """
        result = clickhouse.execute_query(sql)
        formatted_result = [
            {
                "linha": row[0],
                "id_viagem": row[1],
                "duracao_real": row[2],
                "duracao_programada": row[3],
                "diferenca": row[4]
            }
            for row in result
        ]
        return jsonify({"data": formatted_result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route("/api/viagens_dia_semana/<linha>", methods=["GET"])
def viagens_dia_semana(linha):
    """Endpoint para obter a quantidade de viagens por dia da semana para uma linha específica."""
    auth_error = verificar_token()
    if auth_error:
        return auth_error

    try:
        sql = f"""
        SELECT
            linha,
            dia_semana_nome,
            quantidade_viagens
        FROM grupo3.view_viagens_dia_semana
        WHERE linha = '{linha}'
        ORDER BY dia_semana_nome ASC
        """
        result = clickhouse.execute_query(sql)
        formatted_result = [
            {
                "linha": row[0],
                "dia_semana": row[1],
                "quantidade_viagens": row[2]
            }
            for row in result
        ]
        return jsonify({"data": formatted_result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_bp.route("/api/quantidade_viagens_origem/<linha>", methods=["GET"])
def quantidade_viagens_origem(linha):
    """Endpoint para obter a quantidade de viagens com alertas de origem para uma linha específica."""
    auth_error = verificar_token()
    if auth_error:
        return auth_error

    try:
        sql = f"""
        SELECT
            nome_linha,
            estacao_alerta,
            total_flags
        FROM grupo3.view_quantidade_viagens_origem
        WHERE nome_linha = '{linha}'
        ORDER BY total_flags DESC
        """
        result = clickhouse.execute_query(sql)
        formatted_result = [
            {
                "nome_linha": row[0],
                "estacao_alerta": row[1],
                "total_flags": row[2]
            }
            for row in result
        ]
        return jsonify({"data": formatted_result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_bp.route("/api/pcd_origem/<linha>", methods=["GET"])
def pcd_origem(linha):
    """Endpoint para obter a quantidade de PCDs por estação de origem para uma linha específica."""
    auth_error = verificar_token()
    if auth_error:
        return auth_error

    try:
        sql = f"""
        SELECT
            nome_linha,
            estacao_origem,
            total_pcds
        FROM grupo3.view_pcd_origem
        WHERE nome_linha = '{linha}'
        ORDER BY total_pcds DESC
        """
        result = clickhouse.execute_query(sql)
        formatted_result = [
            {
                "nome_linha": row[0],
                "estacao_origem": row[1],
                "total_pcds": row[2]
            }
            for row in result
        ]
        return jsonify({"data": formatted_result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_bp.route("/api/pcd_destino/<linha>", methods=["GET"])
def pcd_destino(linha):
    """Endpoint para obter a quantidade de PCDs por estação de destino para uma linha específica."""
    auth_error = verificar_token()
    if auth_error:
        return auth_error

    try:
        sql = f"""
        SELECT
            nome_linha,
            estacao_destino,
            total_pcds
        FROM grupo3.view_pcd_destino
        WHERE nome_linha = '{linha}'
        ORDER BY total_pcds DESC
        """
        result = clickhouse.execute_query(sql)
        formatted_result = [
            {
                "nome_linha": row[0],
                "estacao_destino": row[1],
                "total_pcds": row[2]
            }
            for row in result
        ]
        return jsonify({"data": formatted_result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_bp.route("/api/quantidade_viagens_destino/<linha>", methods=["GET"])
def quantidade_viagens_destino(linha):
    """Endpoint para obter a quantidade de viagens por estação de destino para uma linha específica."""
    auth_error = verificar_token()
    if auth_error:
        return auth_error

    try:
        sql = f"""
        SELECT
            nome_linha,
            estacao_destino,
            quantidade_viagens
        FROM grupo3.view_quantidade_viagens_destino
        WHERE nome_linha = '{linha}'
        ORDER BY quantidade_viagens DESC
        """
        result = clickhouse.execute_query(sql)
        formatted_result = [
            {
                "nome_linha": row[0],
                "estacao_destino": row[1],
                "quantidade_viagens": row[2]
            }
            for row in result
        ]
        return jsonify({"data": formatted_result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_bp.route("/api/quantidade_viagens_dia_mes/<linha>", methods=["GET"])
def quantidade_viagens_dia_mes(linha):
    """Endpoint para obter a quantidade de viagens por dia do mês para uma linha específica."""
    auth_error = verificar_token()
    if auth_error:
        return auth_error

    try:
        sql = f"""
        SELECT
            dia_mes,
            nome_linha,
            quantidade_viagens
        FROM grupo3.view_quantidade_viagens_dia_mes
        WHERE nome_linha = '{linha}'
        ORDER BY dia_mes ASC
        """
        result = clickhouse.execute_query(sql)
        formatted_result = [
            {
                "dia_mes": row[0],
                "nome_linha": row[1],
                "quantidade_viagens": row[2]
            }
            for row in result
        ]
        return jsonify({"data": formatted_result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_bp.route("/api/alerta_estacao/<linha>", methods=["GET"])
def alerta_estacao(linha):
    """Endpoint para obter o total de flags de alerta por estação para uma linha específica."""
    auth_error = verificar_token()
    if auth_error:
        return auth_error

    try:
        sql = f"""
        SELECT
            nome_linha,
            estacao_alerta,
            total_flags
        FROM grupo3.view_alerta_estacao
        WHERE nome_linha = '{linha}'
        ORDER BY total_flags DESC
        """
        result = clickhouse.execute_query(sql)
        formatted_result = [
            {
                "nome_linha": row[0],
                "estacao_alerta": row[1],
                "total_flags": row[2]
            }
            for row in result
        ]
        return jsonify({"data": formatted_result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_bp.route("/api/quantidade_viagens_origem_destino/<linha>", methods=["GET"])
def quantidade_viagens_origem_destino(linha):
    """Endpoint para obter a quantidade de viagens por estação de origem e destino para uma linha específica."""
    auth_error = verificar_token()
    if auth_error:
        return auth_error

    try:
        sql = f"""
        SELECT
            nome_linha,
            estacao_origem,
            estacao_destino,
            quantidade_viagens
        FROM grupo3.view_quantidade_viagens_origem_destino
        WHERE nome_linha = '{linha}'
        ORDER BY quantidade_viagens DESC
        """
        result = clickhouse.execute_query(sql)
        formatted_result = [
            {
                "nome_linha": row[0],
                "estacao_origem": row[1],
                "estacao_destino": row[2],
                "quantidade_viagens": row[3]
            }
            for row in result
        ]
        return jsonify({"data": formatted_result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def register_routes_linha(app):
    app.register_blueprint(api_bp)