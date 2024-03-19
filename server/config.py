import os
from pathlib import Path

from dotenv import load_dotenv

# Base directory of our application project.
BASE_DIR = Path(__file__).resolve().parent

load_dotenv(dotenv_path=BASE_DIR, override=True)


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ""


class DevelopmentConfig(Config):
    DEBUG = True

    # SQLite database for development environment only.
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")


class TestingConfig(Config):
    # SQLite Database for testing.
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.test.sqlite3"
    TESTING = True
