import flask
from flask_restful import Resource

from rest_utils import json_response
from services.groups_service import *


class GroupListResource(Resource):
    @staticmethod
    def get():
        res = get_all_groups()
        return json_response(res)

    @staticmethod
    def post():
        g_name = flask.request.json["g_name"]
        create_group(g_name)
