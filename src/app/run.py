from flask import Flask
from routes.routes import register_routes
from routes.routes_linha import register_routes_linha

def create_app():
    """
    Cria e configura a aplicação Flask.
    """
    app = Flask(__name__)

    register_routes(app)
    register_routes_linha(app)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
