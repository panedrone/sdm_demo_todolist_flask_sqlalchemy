"""

My hand-coded extension of generated class

"""

from dbal.group import Group
from dbal.groups_dao import GroupsDao


class GroupsDaoEx(GroupsDao):

    def __init__(self, ds):
        self.ds = ds

    def rename(self, g_id, g_name):
        self.ds.filter(Group, {'g_id': g_id}).update(values={'g_name': g_name})
