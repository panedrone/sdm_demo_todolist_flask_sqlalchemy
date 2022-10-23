from dbal.data_store import ds
from dbal.group import Group
from dbal.group_li import GroupLi
from dbal.groups_dao_ex import GroupsDaoEx
from dbal.task import Task

_dao = GroupsDaoEx(ds())


def get_all_groups():
    return ds().get_all_raw(GroupLi)


def get_group(g_id):
    group = _dao.read_group(g_id)
    return group


def create_group(g_name):
    group = Group(g_name=g_name)
    _dao.create_group(group)
    ds().commit()


def update_group(g_id, g_name):
    # group = _dao.read_group(g_id)
    # group.g_name = g_name
    # _dao.update_group(group)
    _dao.rename(g_id, g_name)
    ds().commit()


def delete_group(g_id):
    ds().delete_by_filter(Task, {"g_id": g_id})
    rows_deleted = _dao.delete_group(g_id)
    print(f"rows_deleted: {rows_deleted}")
    ds().commit()
