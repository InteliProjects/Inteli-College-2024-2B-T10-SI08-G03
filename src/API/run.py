from flask import Flask
from flask_cors import CORS
from routes.principal_routes import register_routes as register_routes_default
from routes.line_routes import register_routes as register_routes_linha
from routes.health import health_bp

def create_app():
    """
    Cria e configura a aplicação Flask.
    """
    app = Flask(__name__)
    # Aceitar requisições de qualquer origem
    CORS(app)
    
    # Registra os blueprints
    register_routes_default(app)
    register_routes_linha(app)
    app.register_blueprint(health_bp)

    return app

# A instância 'app' deve ser criada aqui para ser acessível pelo Gunicorn
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
