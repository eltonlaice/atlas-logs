from flask import Flask
from flask_login import LoginManager
from app.routes.auth import auth
from app.models.user import User  # Changed to absolute import

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'  # Set a secret key for sessions
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    @login_manager.user_loader
    def load_user(user_id):
        # This function should return a User object or None
        return User.get(user_id)
    
    app.register_blueprint(auth)
    
    return app
