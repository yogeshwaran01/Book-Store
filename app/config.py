import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Configuration:
    """ Configurations for Flask app """

    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SECRET_KEY = "admin"
    # SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base_dir, "users.db")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_SWATCH = "cerulean"
    BASIC_AUTH_USERNAME = os.environ.get('ADMIN_USER')
    BASIC_AUTH_PASSWORD = os.environ.get('ADMIN_PASS')
    # BASIC_AUTH_USERNAME = "admin"
    # BASIC_AUTH_PASSWORD = "admin"
