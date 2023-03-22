from dbal.data_store import scoped_ds
from dbal.project import Project
from dbal.projects_dao_ex import ProjectsDaoEx
from dbal.task import Task


def get_all_projects():
    ds = scoped_ds()
    return ProjectsDaoEx(ds).get_all_projects()


def read_project(p_id):
    ds = scoped_ds()
    project = ProjectsDaoEx(ds).read_project(p_id)
    return project


def create_project(p_name):
    ds = scoped_ds()
    project = Project(p_name=p_name)
    ProjectsDaoEx(ds).create_project(project)
    ds.commit()


def update_project(p_id, p_name):
    ds = scoped_ds()
    ProjectsDaoEx(ds).rename(p_id, p_name)
    ds.commit()


def delete_project(p_id):
    ds = scoped_ds()
    ds.delete_by_filter(Task, {"p_id": p_id})
    ProjectsDaoEx(ds).delete_project(p_id)
    ds.commit()
