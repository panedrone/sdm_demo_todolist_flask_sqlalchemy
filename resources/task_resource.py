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
        req_json = flask.request.json
        update_task(t_id, req_json)

    @staticmethod
    def delete(t_id):
        delete_task(t_id)
