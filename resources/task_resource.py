import json

import flask
import marshmallow as mm
from flask import Response
from flask_restful import Resource
from marshmallow.validate import Length

from services.tasks_service import *


# noinspection PyTypeChecker
class TaskSchema(mm.Schema):
    # https://stackoverflow.com/questions/54345070/python-marshmallow-not-detecting-error-in-required-field
    # "required" just means "exists in JSON"
    t_date = mm.fields.Str(required=True,
                           allow_none=False,
                           validate=Length(min=1, error="Empty date is not allowed"))
    t_subject = mm.fields.Str(required=True,
                              allow_none=False,
                              validate=Length(min=1, error="Empty subject is not allowed"))
    t_priority = mm.fields.Int(required=True)
    t_comments = mm.fields.Str(required=False)

    # class Meta:
    #     fields = ("t_id", "g_id", "t_date", "t_subject", "t_priority", "t_comments")
    #     model = Task


task_schema = TaskSchema()


class TaskResource(Resource):
    @staticmethod
    def get(t_id):
        task = get_task(t_id)
        return task_schema.dump(task)

    @staticmethod
    def put(t_id):
        req_json = flask.request.json
        try:
            data = task_schema.load(req_json)
        except mm.ValidationError as error:
            return Response(
                json.dumps(error.messages),
                status=400,
            )
        update_task(t_id, data)

    @staticmethod
    def delete(t_id):
        delete_task(t_id)
        return Response(status=204)
