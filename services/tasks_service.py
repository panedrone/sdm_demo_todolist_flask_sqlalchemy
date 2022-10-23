from datetime import datetime

from dbal.data_store import ds
from dbal.task import Task
from dbal.tasks_dao_ex import TasksDaoEx

_dao = TasksDaoEx()


def get_group_tasks(g_id):
    return _dao.get_tasks_by_group(g_id)


def get_task(t_id):
    task = _dao.read_task(t_id)
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
    _dao.create_task(task)
    ds().commit()
    return task


def update_task(task):
    _dao.update_task(task)
    ds().commit()


def delete_task(t_id):
    _dao.delete_task(t_id)
    ds().commit()
