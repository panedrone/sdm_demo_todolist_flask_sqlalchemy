import json

import flask
import marshmallow as mm
from flask import Response
from flask_restful import Resource
from marshmallow.validate import Length

from services.projects_service import *


# noinspection PyTypeChecker
class ProjectSchema(mm.Schema):
    p_id = mm.fields.Str(required=True)
    p_name = mm.fields.Str(required=True,
                           allow_none=False,
                           validate=Length(min=1, max=256, error="Project name a string[1..256] expected"))

    # class Meta:
    #     fields = ("p_id", "p_name")
    #     model = Group


class ProjectResource(Resource):
    @staticmethod
    def get(p_id):
        res = read_project(p_id)
        return ProjectSchema().dump(res)

    @staticmethod
    def put(p_id):
        req_json = flask.request.json
        try:
            data = ProjectSchema().load(req_json)
        except mm.ValidationError as error:
            return Response(
                json.dumps(error.messages),
                status=400,
            )
        p_name = data["p_name"]
        update_project(p_id, p_name)

    @staticmethod
    def delete(p_id):
        delete_project(p_id)
        return Response(status=204)
