import json

import flask
import marshmallow as mm
from flask import Response
from flask_restful import Resource
from marshmallow.validate import Length

from services.tasks_service import *


# noinspection PyTypeChecker
class NewTaskSchema(mm.Schema):
    t_subject = mm.fields.Str(required=True,
                              allow_none=False,
                              validate=Length(min=1, error="Task subject a string[1..256] expected"))


class TaskLiSchema(mm.Schema):
    class Meta:
        fields = ("t_id", "t_date", "t_subject", "t_priority")


class GroupTasksResource(Resource):
    @staticmethod
    def get(g_id):
        res = get_group_tasks(g_id)
        return TaskLiSchema().dump(res, many=True)

    @staticmethod
    def post(g_id):
        req_json = flask.request.json
        try:
            data = NewTaskSchema().load(req_json)
        except mm.ValidationError as error:
            return Response(
                json.dumps(error.messages),
                status=400,
            )
        t_subject = data["t_subject"]
        create_task(g_id, t_subject)
        return Response(status=201)
