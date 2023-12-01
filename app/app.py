#app.py
from flask import Flask
from auth import auth_bp
from profile import profile_bp
from main import main_bp
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from db import db
from models import User

app = Flask(__name__)

# Load configuration from the Config class
app.config.from_object(Config)

# Initialize the SQLAlchemy database
db.init_app(app)
migrate = Migrate(app, db)

# Initialize the Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
