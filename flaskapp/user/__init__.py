from re import I
from flask import Blueprint
from flask_restx import Api
from flaskapp.user.routes import ns

api_blueprint = Blueprint("User Blueprint", __name__)
api = Api(api_blueprint)
api.add_namespace(ns)