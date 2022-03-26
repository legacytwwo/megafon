from flask import Flask
from fastapi import FastAPI
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from fastapi.middleware.cors import CORSMiddleware

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

from models.core import *
from flask_migrate import Migrate

migrate = Migrate(app, db)