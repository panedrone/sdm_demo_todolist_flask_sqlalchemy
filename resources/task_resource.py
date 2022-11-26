import flask
from flask import Response
from flask_restful import Resource
from marshmallow import ValidationError, fields

from app_marshmallow import ma
from services.tasks_service import *


class TaskSchema(ma().Schema):
    # t_date = fields.Str(required=True)
    t_date = fields.Str(required=True)
    t_subject = fields.Str(required=True)
    t_priority = fields.Int(required=True)
    t_comments = fields.Str(required=False)

    class Meta:
        fields = ("t_id", "g_id", "t_date", "t_subject", "t_priority", "t_comments")
        model = Task


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
        except ValidationError as error:
            return Response(
                error.messages,
                status=400,
            )
        update_task(t_id, data)

    @staticmethod
    def delete(t_id):
        delete_task(t_id)
