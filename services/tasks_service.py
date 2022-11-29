from datetime import datetime

from dbal.data_store import scoped_ds
from dbal.task import Task
from dbal.tasks_dao_ex import TasksDaoEx


def get_group_tasks(g_id):
    ds = scoped_ds()
    return TasksDaoEx(ds).get_tasks_by_group(g_id)


def get_task(t_id):
    ds = scoped_ds()
    task = TasksDaoEx(ds).read_task(t_id)
    return task


def create_task(g_id, t_subject):
    ds = scoped_ds()
    task = Task()
    task.g_id = g_id
    task.t_subject = t_subject
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d")
    task.t_date = dt_string
    task.t_priority = 1
    task.t_comments = ''
    TasksDaoEx(ds).create_task(task)
    ds.commit()
    return task


def update_task(t_id: int, data: dict):
    ds = scoped_ds()
    TasksDaoEx(ds).update_task(t_id, data)
    ds.commit()


def delete_task(t_id):
    ds = scoped_ds()
    TasksDaoEx(ds).delete_task(t_id)
    ds.commit()
