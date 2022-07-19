from datetime import datetime

from dbal.data_store import data_store
from dbal.task import Task


def get_group_tasks(g_id):
    tasks = data_store.session.query(Task).filter(Task.g_id == g_id).order_by(Task.t_date, Task.t_id).all()
    return tasks


def get_task(t_id):
    # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_updating_objects.htm
    task = data_store.session.query(Task).get(t_id)
    return task


def create_task(g_id, t_subject):
    task = Task()
    task.g_id = g_id
    task.t_subject = t_subject
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d")
    task.t_date = dt_string
    task.t_priority = 1
    task.t_comments = ''
    data_store.session.add(task)
    data_store.commit()
    return task


def delete_task(t_id):
    # https://stackoverflow.com/questions/26643727/python-sqlalchemy-deleting-with-the-session-object
    data_store.session.query(Task).filter(Task.t_id == t_id).delete()
    data_store.commit()


def update_task(task):
    data_store.commit()
