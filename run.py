from flask import Flask
from app.routes.search import search_bp
from app.utils.search_utils import perform_search
import os

app = Flask(__name__)

# Load configuration from environment variables
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')
app.config['MONGODB_URI'] = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/atlas_logs')

# Register blueprints
app.register_blueprint(search_bp)
app.template_folder = 'app/templates'

if __name__ == '__main__':
    app.run(debug=True)
