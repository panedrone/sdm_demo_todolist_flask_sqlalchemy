import json

import flask
import marshmallow as mm
from flask import Response
from flask_restful import Resource
from marshmallow.validate import Length, Validator, Range

from services.tasks_service import *


class MyDateStringValidator(Validator):
    def __init__(self, error: str):
        self.error = error

    def __call__(self, value: str) -> str:
        try:
            dt = datetime.strptime(value, '%Y-%m-%d').date()
        except Exception:
            raise mm.ValidationError(self.error)
        if str(dt) != value:
            raise mm.ValidationError(self.error)
        return value


# noinspection PyTypeChecker
class TaskSchema(mm.Schema):
    t_date = mm.fields.Str(required=True,
                           allow_none=False,
                           validate=MyDateStringValidator("Task date format expected is 'yyyy-mm-dd' -> '2022-01-01'"))
    t_subject = mm.fields.Str(required=True,
                              allow_none=False,
                              validate=Length(min=1, max=256, error="Task subject a string[1..256] expected"))
    t_priority = mm.fields.Int(required=True,
                               validate=Range(1, 10, error="Task priority an integer 1..10 expected"))
    t_comments = mm.fields.Str(required=False)

    # class Meta:
    #     fields = ("t_id", "g_id", "t_date", "t_subject", "t_priority", "t_comments")
    #     model = Task


class TaskResource(Resource):
    @staticmethod
    def get(t_id):
        task = get_task(t_id)
        return TaskSchema().dump(task)

    @staticmethod
    def put(t_id):
        req_json = flask.request.json
        try:
            data = TaskSchema().load(req_json)
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
