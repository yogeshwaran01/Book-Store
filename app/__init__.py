from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_basicauth import BasicAuth

from .config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

database = SQLAlchemy(app)

migrate = Migrate(app, db=database)

admin = Admin(app, name="ADMIN")

auth = BasicAuth(app)

from .models import *
from .views import *
