import flask
from flask_restful import Resource

from app_marshmallow import ma
from services.tasks_service import *


class TaskLiSchema(ma().Schema):
    class Meta:
        fields = ("t_id", "t_date", "t_subject", "t_priority")
        # exclude = ("t_comments",)
        model = Task


task_li_schema = TaskLiSchema()


class GroupTasksResource(Resource):
    @staticmethod
    def get(g_id):
        res = get_group_tasks(g_id)
        return task_li_schema.dump(res, many=True)

    @staticmethod
    def post(g_id):
        t_subject = flask.request.json["t_subject"]
        create_task(g_id, t_subject)
