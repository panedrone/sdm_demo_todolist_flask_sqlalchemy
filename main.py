from app import *
from dal.data_store import DataStore
from rest_utils import to_json_str
from services.groups_service import GroupsService
from services.tasks_service import TasksService

ds = DataStore()

groups_svc = GroupsService(ds)
tasks_svc = TasksService(ds)


class GroupListResource(flask_restful.Resource):
    @staticmethod
    def get():
        res = groups_svc.get_groups()
        return to_json_str(res)

    @staticmethod
    def post():
        g_name = flask.request.json["g_name"]
        groups_svc.create_group(g_name)


class GroupResource(flask_restful.Resource):
    @staticmethod
    def get(g_id):
        res = groups_svc.get_group(g_id)
        return to_json_str(res)

    @staticmethod
    def put(g_id):
        g_name = flask.request.json["g_name"]
        groups_svc.update_group(g_id, g_name)

    @staticmethod
    def delete(g_id):
        groups_svc.delete_group(g_id)


class GroupTasksResource(flask_restful.Resource):
    @staticmethod
    def get(g_id):
        res = tasks_svc.get_group_tasks(g_id)
        return to_json_str(res)

    @staticmethod
    def post(g_id):
        t_subject = flask.request.json["t_subject"]
        tasks_svc.create_task(g_id, t_subject)


class TaskResource(flask_restful.Resource):
    @staticmethod
    def get(t_id):
        task = tasks_svc.get_task(t_id)
        return to_json_str(task)

    @staticmethod
    def put(t_id):
        task = tasks_svc.get_task(t_id)
        inp = flask.request.json
        task.t_date = inp["t_date"]
        task.t_subject = inp["t_subject"]
        task.t_priority = inp["t_priority"]
        task.t_comments = inp["t_comments"]
        tasks_svc.update_task(task)

    @staticmethod
    def delete(t_id):
        tasks_svc.delete_task(t_id)


api.add_resource(GroupListResource, "/groups")
api.add_resource(GroupResource, "/group/<g_id>")
api.add_resource(GroupTasksResource, '/group/<g_id>/tasks')
api.add_resource(TaskResource, '/task/<t_id>')


@app.route("/")
def home():
    return flask.render_template("index.html")


if __name__ == "__main__":  # on running python main.py
    app.run(debug=True)
