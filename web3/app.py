# app.py (en raíz de tu proyecto)
from flask import Flask
from flask_cors import CORS
from backend.config import DevelopmentConfig
from backend.routes.main import main_bp
from backend.routes.donations import donations_bp
import logging
from logging.handlers import RotatingFileHandler
import os

def create_app():
    app = Flask(
        __name__,
        static_folder="static",  # cambiamos esto para reflejar tu estructura actual
        template_folder="templates"
    )
    app.config.from_object(DevelopmentConfig)
    CORS(app)

    # Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(donations_bp)

    # Logging setup
    if not os.path.exists("logs"):
        os.mkdir("logs")

    handler = RotatingFileHandler("logs/app.log", maxBytes=100000, backupCount=1)
    handler.setFormatter(logging.Formatter(
        "[%(asctime)s] [%(levelname)s] - %(message)s"
    ))
    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(logging.INFO)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
