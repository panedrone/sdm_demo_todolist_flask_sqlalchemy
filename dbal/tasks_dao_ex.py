"""

My hand-coded extension of generated class

"""
from dbal.data_store import ds
from dbal.task import Task
from dbal.tasks_dao import TasksDao


class TasksDaoEx(TasksDao):

    def __init__(self):
        super().__init__(ds())

    def get_tasks_by_group(self, g_id):
        tasks = self.ds.filter(Task, {'g_id': g_id}).order_by(Task.t_date, Task.t_id).all()
        return tasks

    def update_task(self, t_id, data: dict):
        self.ds.filter(Task, {'t_id': t_id}).update(values=data)
