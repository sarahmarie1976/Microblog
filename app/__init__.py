from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
app.config.from_object(Config)  # Load config from Config class

db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)
login = LoginManager(app)

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))


from app import routes, models
