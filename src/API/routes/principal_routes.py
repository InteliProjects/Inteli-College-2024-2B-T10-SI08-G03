from flask import Blueprint, request, jsonify
from services.clickhouse_service import ClickHouseService
import os

api_bp = Blueprint("api", __name__)
clickhouse_service = ClickHouseService()
API_TOKEN = os.getenv("API_TOKEN")

def verificar_token():
    token = request.headers.get("Authorization")
    if not token or token != f"Bearer {API_TOKEN}":
        return jsonify({"error": "Token inválido ou ausente"}), 401
    return None

@api_bp.route("/api/qtd_viagens_por_linha", methods=["GET"])
def qtd_viagens_por_linha():
    """Endpoint para obter a quantidade de viagens por linha."""
    auth_error = verificar_token()
    if auth_error:
        return auth_error
    
    init_date = request.args.get('init_date')  # Exemplo: /api/duracao_media?init_date=2024-01-01
    final_date = request.args.get('final_date')  # Exemplo: /api/duracao_media?final_date=2024-12-31

    try:
        # Construindo a consulta SQL base
        sql = """
        SELECT 
            travel_date,
            line,
            total_travels
        FROM grupo3.viagens_por_linha
        WHERE 1=1
        """
        
        # Condicionalmente adicionar filtros de data à consulta
        if init_date:
            sql += f" AND travel_date >= '{init_date}'"
        if final_date:
            sql += f" AND travel_date <= '{final_date}'"
        
        # Executando a consulta no banco de dados
        result = clickhouse_service.execute_query(sql)
        
        # Formatando o resultado
        formatted_result = [
            {"line": row[1], "total_travels": row[2]} 
            for row in result
        ]
        
        # Retornando a resposta
        return jsonify({"data": formatted_result}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route("/api/duracao_media", methods=["GET"])
def duracao_media():
    """Endpoint para obter a duração média das viagens por linha ao longo do tempo."""
    auth_error = verificar_token()
    if auth_error:
        return auth_error

    init_date = request.args.get('init_date')  # Exemplo: /api/duracao_media?init_date=2024-01-01
    final_date = request.args.get('final_date')  # Exemplo: /api/duracao_media?final_date=2024-12-31
    try:
        sql = """
        SELECT
            data_operacional,
            linha,
            duracao_media
        FROM grupo3.viagem_duracao_media
        WHERE 1=1
        """
        
        if init_date:
            sql += f" AND data_operacional >= '{init_date}'"
        if final_date:
            sql += f" AND data_operacional <= '{final_date}'"

        sql += " ORDER BY data_operacional ASC, linha ASC"

        result = clickhouse_service.execute_query(sql)
   
        formatted_result = [
            {
                "data_operacional": str(row[0]),
                "linha": row[1],
                "duracao_media": row[2]
            }
            for row in result
        ]
        
        return jsonify({"data": formatted_result}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_bp.route("/api/duracao_real_programada", methods=["GET"])
def duracao_real_programada():
    """Endpoint para obter a duração real e programada das viagens por linha."""
    auth_error = verificar_token()
    if auth_error:
        return auth_error

    try:
        sql = """
        SELECT
            duracao_real,
            duracao_programada,
            linha
        FROM grupo3.viagem_estimada_viagem_real
        ORDER BY linha ASC
        """
        result = clickhouse_service.execute_query(sql)
        formatted_result = [
            {
                "duracao_real": row[0],
                "duracao_programada": row[1],
                "linha": row[2]
            }
            for row in result
        ]
        return jsonify({"data": formatted_result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route("/api/taxa_atraso", methods=["GET"])
def taxa_atraso():
    """Endpoint para obter a taxa de atraso por linha."""
    auth_error = verificar_token()
    if auth_error:
        return auth_error

    try:
        sql = """
        SELECT
            linha,
            viagens_atrasadas,
            total_viagens,
            taxa_atraso
        FROM grupo3.taxa_atraso_por_linha
        ORDER BY taxa_atraso DESC
        """
        result = clickhouse_service.execute_query(sql)
        formatted_result = [
            {
                "linha": row[0],
                "viagens_atrasadas": row[1],
                "total_viagens": row[2],
                "taxa_atraso": row[3]
            }
            for row in result
        ]
        return jsonify({"data": formatted_result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@api_bp.route("/api/viagens_por_dia_mes", methods=["GET"])
def viagens_por_dia_mes():
    """Endpoint para obter a quantidade de viagens por dia do mês."""
    auth_error = verificar_token()
    if auth_error:
        return auth_error

    try:
        sql = """
        SELECT
            dia_mes,
            quantidade_viagens
        FROM grupo3.viagens_por_dia_mes
        ORDER BY dia_mes
        """
        result = clickhouse_service.execute_query(sql)
        formatted_result = [
            {"dia_mes": row[0], "quantidade_viagens": row[1]} for row in result
        ]
        return jsonify({"data": formatted_result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route("/api/qtd_viagens_semana_linha", methods=["GET"])
def qtd_viagens_semana_linha():
    """Endpoint para obter a quantidade de viagens por dia da semana agrupadas por linha."""
    auth_error = verificar_token()
    if auth_error:
        return auth_error

    try:
        sql = """
        SELECT
            linha,
            dia_semana_nome,
            quantidade_viagens
        FROM grupo3.qtd_viagens_semana_linha
        ORDER BY
            linha ASC,
            CASE
                WHEN dia_semana_nome = 'domingo' THEN 1
                WHEN dia_semana_nome = 'segunda' THEN 2
                WHEN dia_semana_nome = 'terça' THEN 3
                WHEN dia_semana_nome = 'quarta' THEN 4
                WHEN dia_semana_nome = 'quinta' THEN 5
                WHEN dia_semana_nome = 'sexta' THEN 6
                WHEN dia_semana_nome = 'sábado' THEN 7
            END ASC
        """
        result = clickhouse_service.execute_query(sql)
        formatted_result = [
            {
                "linha": row[0],
                "dia_semana_nome": row[1],
                "quantidade_viagens": row[2]
            }
            for row in result
        ]
        return jsonify({"data": formatted_result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route("/api/alertas_pcd_por_linha", methods=["GET"])
def alertas_pcd_por_linha():
    """Endpoint para obter o total de alertas PCD por linha."""
    auth_error = verificar_token()
    if auth_error:
        return auth_error

    try:
        sql = """
        SELECT
            line AS linha,
            total_alertas
        FROM grupo3.alertas_pcd_por_linha
        ORDER BY total_alertas DESC
        """
        result = clickhouse_service.execute_query(sql)
        formatted_result = [
            {"linha": row[0], "total_alertas": row[1]} for row in result
        ]
        return jsonify({"data": formatted_result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route("/api/qtd_pcd_semana_linha", methods=["GET"])
def qtd_pcd_semana_linha():
    """Endpoint para obter a quantidade de passageiros PCD por dia da semana e por linha."""
    auth_error = verificar_token()
    if auth_error:
        return auth_error

    try:
        sql = """
        SELECT
            line AS linha,
            dia_semana,
            total_pcds
        FROM grupo3.qtd_pcd_semana_linha
        ORDER BY dia_semana_num ASC, linha ASC
        """
        result = clickhouse_service.execute_query(sql)
        formatted_result = [
            {"linha": row[0], "dia_semana": row[1], "total_pcds": row[2]} for row in result
        ]
        return jsonify({"data": formatted_result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@api_bp.route("/api/qtd_pcd_por_dia", methods=["GET"])
def qtd_pcd_por_dia():
    """Endpoint para obter a quantidade de passageiros PCD por dia da semana."""
    auth_error = verificar_token()
    if auth_error:
        return auth_error

    try:
        sql = """
        SELECT
            dia_semana_nome,
            total_pcds
        FROM grupo3.qtd_pcd_por_dia
        ORDER BY dia_semana_nome ASC
        """
        result = clickhouse_service.execute_query(sql)
        formatted_result = [
            {"dia_semana_nome": row[0], "total_pcds": row[1]} for row in result
        ]
        return jsonify({"data": formatted_result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500




def register_routes(app):
    app.register_blueprint(api_bp)