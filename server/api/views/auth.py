from flask import Blueprint

auth = Blueprint("auth", __name__, template_folder="templates")


@auth.get("/register")
def register():
    return "Register API"
