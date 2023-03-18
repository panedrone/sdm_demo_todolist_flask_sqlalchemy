import logging
import os

import flask
import flask_sqlalchemy
from flask import Blueprint, send_from_directory
from flask_restful import Api

from dbal.data_store import init_ds

flask_app = flask.Flask(__name__)

blueprint = Blueprint('api', __name__, url_prefix='')

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
    return send_from_directory('static', "index.html")


@flask_app.route('/static')
def get_static(path):
    return send_from_directory('static', path)


def add_resources(root):
    from resources.group_resource import GroupResource
    from resources.group_tasks_resource import GroupTasksResource
    from resources.group_list_resource import GroupListResource
    from resources.task_resource import TaskResource

    root.add_resource(GroupListResource, "/groups")
    root.add_resource(GroupResource, "/groups/<int:g_id>")
    root.add_resource(GroupTasksResource, '/groups/<int:g_id>/tasks')
    root.add_resource(TaskResource, '/tasks/<int:t_id>')


if __name__ == "__main__":  # on running python main.py
    db = flask_sqlalchemy.SQLAlchemy(flask_app)

    init_ds(db)
    # init_marshmallow(flask_app)

    add_resources(api)

    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    flask_app.run(debug=True)
