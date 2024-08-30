# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_login import LoginManager
from celery import Celery

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
celery = Celery(__name__)
login_manager = LoginManager()

def create_app(config_class='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    
    # Importar y registrar rutas aquí para evitar importación circular
    with app.app_context():
        from app import routes  # Importar rutas aquí para evitar el problema de importación circular
    
        # Configuración de Celery
        celery.conf.update(app.config)
        
        @login_manager.user_loader
        def load_user(user_id):
            from app.models import User  # Importar el modelo aquí para evitar problemas de importación circular
            return User.query.get(int(user_id))
        
        login_manager.init_app(app)
        login_manager.login_view = 'main.login'
        
        # Registrar blueprints
        app.register_blueprint(routes.bp)
    
    return app
