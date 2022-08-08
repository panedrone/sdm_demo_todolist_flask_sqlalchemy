from datetime import datetime

from dbal.data_store import ds
from dbal.task import Task

_dao = TasksDao(ds())

def get_group_tasks(g_id):
    # tasks = session().query(Task).filter(Task.g_id == g_id).order_by(Task.t_date, Task.t_id).all()
    tasks = ds().filter(Task, {'g_id': g_id}).order_by(Task.t_date, Task.t_id).all()
    return tasks


def get_task(t_id):
    # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_updating_objects.htm
    # task = session().query(Task).get(t_id)
    # task = session().query(Task).get({"t_id": t_id})
    task = ds().get_one(Task, {"t_id": t_id})
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
    ds().create(task)
    ds().commit()
    return task


def update_task(task):
    ds().commit()


def delete_task(t_id):
    # https://stackoverflow.com/questions/26643727/python-sqlalchemy-deleting-with-the-session-object
    # session().query(Task).filter(Task.t_id == t_id).delete()
    # session().query(Task).filter_by(**{"t_id": t_id}).delete()
    ds().delete_one(Task, {"t_id": t_id})
    # session().delete(Task(t_id=t_id)) # InvalidRequestError: Instance '<Task at 0x21404f8f6a0>' is not persisted
    ds().commit()
