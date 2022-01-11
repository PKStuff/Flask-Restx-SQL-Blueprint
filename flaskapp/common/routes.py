from flaskapp import app
from flask import Blueprint

api = Blueprint('Common', __name__)

@api.route('/')
def index():
    return "Common API's"