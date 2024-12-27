from flask import Blueprint, jsonify
from etl_pipeline import EtlPipeline

routes = Blueprint("routes", __name__)
pipeline = EtlPipeline()

@routes.route("/etl/intervalos", methods=["POST"])
def run_intervalos():
    pipeline.run_intervalos()
    return jsonify({"status": "success", "message": " ETL Intervalo completed successfully"})

@routes.route("/etl/pcd", methods=["POST"])
def run_pcd():
    pipeline.run_pcd()
    return jsonify({"status": "success", "message": " ETL PCD completed successfully"})

@routes.route("/etl/viagens", methods=["POST"])
def run_viagens():
    pipeline.run_viagens()
    return jsonify({"status": "success", "message": "ETL Viagens completed successfully"})

@routes.route("/etl/all", methods=["POST"])
def run_all():
    pipeline.run_all()
    return jsonify({"status": "success", "message": "ETL para todas as tabelas concluído com sucesso"})