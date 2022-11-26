import flask
from flask_restful import Resource

from app_marshmallow import ma
from services.groups_service import *


class GroupLiSchema(ma().Schema):
    class Meta:
        fields = ("g_id", "g_name", "g_tasks_count")
        model = GroupLi


group_li_schema = GroupLiSchema()


class GroupListResource(Resource):
    @staticmethod
    def get():
        res = get_all_groups()
        return group_li_schema.dump(res, many=True)

    @staticmethod
    def post():
        g_name = flask.request.json["g_name"]
        create_group(g_name)
