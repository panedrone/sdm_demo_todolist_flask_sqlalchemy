from dbal.data_store import scoped_ds
from dbal.group import Group
from dbal.group_li import GroupLi
from dbal.groups_dao_ex import GroupsDaoEx
from dbal.task import Task


def get_all_groups():
    ds = scoped_ds()
    return ds.get_all_raw(GroupLi)


def get_group(g_id):
    ds = scoped_ds()
    group = GroupsDaoEx(ds).read_group(g_id)
    return group


async def create_group(g_name):
    ds = scoped_ds()
    group = Group(g_name=g_name)
    GroupsDaoEx(ds).create_group(group)
    ds.commit()


async def update_group(g_id, g_name):
    ds = scoped_ds()
    # group = _dao.read_group(g_id)
    # group.g_name = g_name
    # _dao.update_group(group)
    GroupsDaoEx(ds).rename(g_id, g_name)
    ds.commit()


async def delete_group(g_id):
    ds = scoped_ds()
    ds.delete_by_filter(Task, {"g_id": g_id})
    rows_deleted = GroupsDaoEx(ds).delete_group(g_id)
    print(f"rows_deleted: {rows_deleted}")
    ds.commit()
