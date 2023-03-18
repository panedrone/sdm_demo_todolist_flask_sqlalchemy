import json

import flask
import marshmallow as mm
from flask import Response
from flask_restful import Resource
from marshmallow.validate import Length

from services.groups_service import *


# noinspection PyTypeChecker
class GroupSchema(mm.Schema):
    g_name = mm.fields.Str(required=True,
                           allow_none=False,
                           validate=Length(min=1, max=256, error="Group name a string[1..256] expected"))

    # class Meta:
    #     fields = ("g_id", "g_name")
    #     model = Group


class GroupResource(Resource):
    @staticmethod
    def get(g_id):
        res = get_group(g_id)
        return GroupSchema().dump(res)

    @staticmethod
    def put(g_id):
        req_json = flask.request.json
        try:
            data = GroupSchema().load(req_json)
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
        return Response(status=204)
