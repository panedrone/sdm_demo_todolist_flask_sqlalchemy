import flask
from flask import Blueprint
from flask_restful import Api

from app import app
from resources.group_resource import GroupResource
from resources.group_tasks_resource import GroupTasksResource
from resources.group_list_resource import GroupListResource
from resources.task_resource import TaskResource

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint)

app.register_blueprint(blueprint)

api.add_resource(GroupListResource, "/groups")
api.add_resource(GroupResource, "/groups/<int:g_id>")
api.add_resource(GroupTasksResource, '/groups/<int:g_id>/tasks')
api.add_resource(TaskResource, '/tasks/<int:t_id>')


@app.route("/")
def home():
    return flask.render_template("index.html")


if __name__ == "__main__":  # on running python main.py
    app.run(debug=True)
