from flask import Blueprint

manager = Blueprint("manager", __name__, template_folder="templates")


@manager.get("/")
def index():
    return "API Index"
