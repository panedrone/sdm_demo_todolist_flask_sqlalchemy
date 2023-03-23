from datetime import datetime

from dbal.data_store import scoped_ds
from dbal.task import Task
from dbal.tasks_dao_ex import TasksDao


def get_tasks_by_project(p_id):
    ds = scoped_ds()
    return TasksDao(ds).get_project_tasks(p_id)


def read_task(t_id):
    ds = scoped_ds()
    task = TasksDao(ds).read_task(t_id)
    return task


def create_task(p_id, t_subject):
    ds = scoped_ds()
    task = Task()
    task.p_id = p_id
    task.t_subject = t_subject
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d")
    task.t_date = dt_string
    task.t_priority = 1
    task.t_comments = ''
    TasksDao(ds).create_task(task)
    ds.commit()
    return task


def update_task(t_id: int, data: dict):
    ds = scoped_ds()
    TasksDao(ds).update_task(t_id, data)
    ds.commit()


def delete_task(t_id):
    ds = scoped_ds()
    TasksDao(ds).delete_task(t_id)
    ds.commit()
