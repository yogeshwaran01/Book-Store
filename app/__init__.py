from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_basicauth import BasicAuth

from .config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

database = SQLAlchemy(app)
migrate = Migrate(app, database)

admin = Admin(app, name="ADMIN", template_mode="bootstarp3")

auth = BasicAuth(app)

from .models.content import *
from .models.books import *
from .models.contact import *
from .models.blogs import *
from .views import *
