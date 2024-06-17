"""

My hand-coded extension of generated class

"""

from dbal._tasks_dao import _TasksDao
from dbal.task_li import TaskLi


class TasksDao(_TasksDao):

    def __init__(self, ds):
        super().__init__(ds)

    def get_project_tasks(self, p_id):
        q = self.ds.get_query(TaskLi)

        # q = q.filter_by(p_id=p_id) # --- OK
        # q = q.filter_by(TaskLi.p_id = p_id) # --- FAIL
        # q = q.filter_by(TaskLi.p_id == p_id)  # --- FAIL at runtime

        # https://docs.sqlalchemy.org/en/14/core/tutorial.html#operators
        q = q.filter(TaskLi.p_id == p_id)  # --- OK

        q = q.order_by(TaskLi.t_date, TaskLi.t_id)  # --- OK

        # What is the difference between with_entities and load_only in SQLAlchemy?
        # https://stackoverflow.com/questions/47192428/what-is-the-difference-between-with-entities-and-load-only-in-sqlalchemy

        q = q.with_entities(TaskLi.t_id, TaskLi.t_date, TaskLi.t_subject, TaskLi.t_priority)  # not before filter_by!!!

        # SELECT tasks.t_id AS tasks_t_id, tasks.t_date AS tasks_t_date, tasks.t_subject AS tasks_t_subject,
        # tasks.t_priority AS tasks_t_priority
        # FROM tasks
        # WHERE tasks.p_id = ? ORDER BY tasks.t_date, tasks.t_id

        # q = q.with_entities(TaskLi) # --- FAIL
        #
        # tasks.t_id AS tasks_t_id, tasks.p_id AS tasks_p_id, tasks.t_priority AS tasks_t_priority,
        # tasks.t_date AS tasks_t_date, tasks.t_subject AS tasks_t_subject, tasks.t_comments AS tasks_t_comments
        # FROM tasks
        # WHERE tasks.p_id = ? ORDER BY tasks.t_date, tasks.t_id

        tasks = q.all()

        return tasks
