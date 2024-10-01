from flask import Flask
from app.routes.auth import auth_bp
from app.routes.search import search_bp
def create_app():
    app = Flask(__name__)
    
    # Register the auth blueprint
    app.register_blueprint(auth_bp)
    app.register_blueprint(search_bp)
    
    return app
