import flask
from flask_restful import Resource

from app_marshmallow import ma
from services.groups_service import *


class GroupSchema(ma().Schema):
    class Meta:
        fields = ("g_id", "g_name")
        model = Group


group_schema = GroupSchema()


class GroupResource(Resource):
    @staticmethod
    def get(g_id):
        res = get_group(g_id)
        return group_schema.dump(res)

    @staticmethod
    def put(g_id):
        g_name = flask.request.json["g_name"]
        update_group(g_id, g_name)

    @staticmethod
    def delete(g_id):
        delete_group(g_id)
