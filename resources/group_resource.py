import json

import flask
from flask import Response
from flask_restful import Resource
import marshmallow as mm
from marshmallow.validate import Length

from services.groups_service import *


# noinspection PyTypeChecker
class GroupSchema(mm.Schema):
    # https://stackoverflow.com/questions/54345070/python-marshmallow-not-detecting-error-in-required-field
    # "required" just means "exists in JSON"
    g_name = mm.fields.Str(required=True,
                           allow_none=False,
                           validate=Length(min=1, error="Group name is missing"))

    # class Meta:
    #     fields = ("g_id", "g_name")
    #     model = Group


group_schema = GroupSchema()


class GroupResource(Resource):
    @staticmethod
    def get(g_id):
        res = get_group(g_id)
        return group_schema.dump(res)

    @staticmethod
    def put(g_id):
        req_json = flask.request.json
        try:
            data = group_schema.load(req_json)
        except mm.ValidationError as error:
            return Response(
                json.dumps(error.messages),
                status=400,
            )
        g_name = data["g_name"]
        update_group(g_id, g_name)

    @staticmethod
    def delete(g_id):
        delete_group(g_id)
