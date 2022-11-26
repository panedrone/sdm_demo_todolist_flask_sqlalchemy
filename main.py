import os

import flask
import flask_sqlalchemy
from flask import Blueprint
from flask_restful import Api

from app import init_ds
from app_marshmallow import init_marshmallow

flask_app = flask.Flask(__name__)

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint)

flask_app.register_blueprint(blueprint)

# .......................

dir_path = os.path.dirname(os.path.realpath(__file__))

flask_app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{dir_path}/todolist.sqlite"

# add mysql-connector-python to requirements.txt
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:sa@localhost/todolist'

# add psycopg2 to requirements.txt
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sa@localhost/my-tests'

# add cx_oracle to requirements.txt
# if cx_Oracle:
#     user = 'MY_TESTS'
#     pwd = 'sa'
#     dsn = cx_Oracle.makedsn(
#         'localhost', 1521,
#         service_name="orcl"
#         # service_name='your_service_name_if_any'
#     )
#     app.config['SQLALCHEMY_DATABASE_URI'] = f'oracle+cx_oracle://{user}:{pwd}@{dsn}'

# FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds
# significant overhead and will be disabled by default in the future.
# Set it to True or False to suppress this warning.
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@flask_app.route("/")
def home():
    return flask.render_template("index.html")


def add_resources(api):
    from resources.group_resource import GroupResource
    from resources.group_tasks_resource import GroupTasksResource
    from resources.group_list_resource import GroupListResource
    from resources.task_resource import TaskResource

    api.add_resource(GroupListResource, "/groups")
    api.add_resource(GroupResource, "/groups/<int:g_id>")
    api.add_resource(GroupTasksResource, '/groups/<int:g_id>/tasks')
    api.add_resource(TaskResource, '/tasks/<int:t_id>')


if __name__ == "__main__":  # on running python main.py
    db = flask_sqlalchemy.SQLAlchemy(flask_app)
    init_ds(db)
    init_marshmallow(flask_app)
    add_resources(api)
    flask_app.run(debug=True)
