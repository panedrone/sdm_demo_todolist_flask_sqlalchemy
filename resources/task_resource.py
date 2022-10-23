import flask
from flask_restful import Resource

from rest_utils import json_response
from services.tasks_service import *


class TaskResource(Resource):
    @staticmethod
    def get(t_id):
        task = get_task(t_id)
        return json_response(task)

    @staticmethod
    def put(t_id):
        # TODO update without fetch
        task = get_task(t_id)
        inp = flask.request.json
        task.t_date = inp["t_date"]
        task.t_subject = inp["t_subject"]
        task.t_priority = inp["t_priority"]
        task.t_comments = inp["t_comments"]
        update_task(task)

    @staticmethod
    def delete(t_id):
        delete_task(t_id)
