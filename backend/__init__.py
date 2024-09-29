from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from backend.main.config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    with app.app_context():
        from .main import models
        from .auth import bp as auth_bp
        app.register_blueprint(auth_bp, url_prefix='/auth')
        from .main import bp as main_bp
        app.register_blueprint(main_bp)

    return app
