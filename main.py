import flask
from flask_restful import Api

from app import app
from resources.group_resource import GroupResource
from resources.group_tasks_resource import GroupTasksResource
from resources.group_list_resource import GroupListResource
from resources.task_resource import TaskResource

api = Api(app)

api.add_resource(GroupListResource, "/groups")
api.add_resource(GroupResource, "/groups/<int:g_id>")
api.add_resource(GroupTasksResource, '/groups/<int:g_id>/tasks')
api.add_resource(TaskResource, '/tasks/<int:t_id>')


@app.route("/")
def home():
    return flask.render_template("index.html")


# @app.get("/groups2")
# def get_groups():
#     res = get_groups()
#     return to_json_str(res)
#
#
# @app.get("/groups2/<int:g_id>/tasks")
# def get_group_tasks(g_id):
#     res = get_group_tasks(g_id)
#     return to_json_str(res)


if __name__ == "__main__":  # on running python main.py
    app.run(debug=True)
