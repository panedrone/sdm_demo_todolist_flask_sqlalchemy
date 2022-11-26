import flask
from flask_restful import Resource

from app_marshmallow import ma
from services.tasks_service import *


class TaskSchema(ma().Schema):
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
        update_task(t_id, req_json)

    @staticmethod
    def delete(t_id):
        delete_task(t_id)
