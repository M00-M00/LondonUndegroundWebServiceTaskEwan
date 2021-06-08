
from flask import Flask, current_app
from numpy import apply_over_axes
from config import Config
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy, sqlalchemy
from flask_migrate import Migrate
import logging
import os
from flask_cors import CORS, cross_origin

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app

