from flask import Flask
from flask_login import LoginManager
from app.models.user import User  # Changed to absolute import
from app.routes.search import search_bp


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'  # Set a secret key for sessions

    app.register_blueprint(search_bp)

    return app
