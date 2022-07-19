import flask
from flask_restful import Resource

from rest_utils import to_json_str
from services.groups_service import *


class GroupListResource(Resource):
    @staticmethod
    def get():
        res = get_groups()
        return to_json_str(res)

    @staticmethod
    def post():
        g_name = flask.request.json["g_name"]
        create_group(g_name)
