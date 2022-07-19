import flask
from flask_restful import Resource

from rest_utils import json_response
from services.tasks_service import *


class GroupTasksResource(Resource):
    @staticmethod
    def get(g_id):
        res = get_group_tasks(g_id)
        return json_response(res)

    @staticmethod
    def post(g_id):
        t_subject = flask.request.json["t_subject"]
        create_task(g_id, t_subject)
