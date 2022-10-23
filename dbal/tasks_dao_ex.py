"""

My hand-coded extension of generated class

"""
from dbal.task import Task
from dbal.tasks_dao import TasksDao


class TasksDaoEx(TasksDao):

    def __init__(self, ds):
        self.ds = ds

    def get_tasks_by_group(self, g_id):
        tasks = self.ds.filter(Task, {'g_id': g_id}).order_by(Task.t_date, Task.t_id).all()
        return tasks
