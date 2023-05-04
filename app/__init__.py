from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    #makes flask recognize our bp
    # do this each time we make a new bp
    from .route import books_bp
    app.register_blueprint(books_bp)


    return app