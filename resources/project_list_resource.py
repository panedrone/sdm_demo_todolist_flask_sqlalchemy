import json

import flask
import marshmallow as mm
from flask import Response
from flask_restful import Resource
from marshmallow.validate import Length

from services.projects_service import *


# noinspection PyTypeChecker
class NewProjectSchema(mm.Schema):
    # https://stackoverflow.com/questions/54345070/python-marshmallow-not-detecting-error-in-required-field
    # "required" just means "exists in JSON"
    p_name = mm.fields.Str(required=True,
                           allow_none=False,
                           validate=Length(min=1, max=256, error="Project name a string[1..256] expected"))

    # class Meta:
    #     fields = ("p_name",)


class ProjectLiSchema(mm.Schema):
    class Meta:
        fields = ("p_id", "p_name", "p_tasks_count")


class ProjectListResource(Resource):
    @staticmethod
    def get():
        res = get_all_projects()
        return ProjectLiSchema().dump(res, many=True)

    @staticmethod
    def post():
        req_json = flask.request.json
        try:
            data = NewProjectSchema().load(req_json)
        except mm.ValidationError as error:
            return Response(
                json.dumps(error.messages),
                status=400,
            )
        p_name = data["p_name"]
        create_project(p_name)
        return Response(status=201)
