# backend/config.py
import os

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret")
    LOG_FILE = "logs/app.log"

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass
