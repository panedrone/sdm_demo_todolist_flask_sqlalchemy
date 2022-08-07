from dbal.data_store import ds, session
from dbal.group import Group
from dbal.group_li import GroupLi
from dbal.task import Task


def get_all_groups():
    # https://stackoverflow.com/questions/17972020/how-to-execute-raw-sql-in-flask-sqlalchemy-app
    # user = session.query(User).from_statement(
    #     text("""SELECT * FROM users where name=:name""")
    # ).params(name="ed").all()

    # query = self.ds.engine.execute(GroupExModel.SQL) # it returns an array of tuples
    # return query.all()

    # m: GroupEx = None

    return ds().get_all(GroupLi)

    # return GroupsDao(self.ds).get_groups(GroupEx.SQL)


def get_group(g_id):
    # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_updating_objects.htm
    group = session().query(Group).get(g_id)
    return group


def create_group(g_name):
    group = Group(g_name=g_name)
    session().add(group)
    ds().commit()


def update_group(g_id, g_name):
    # https://code-maven.com/slides/python/orm-update
    group = session().query(Group).get(g_id)
    group.g_name = g_name
    ds().commit()


def delete_group(g_id):
    # https://stackoverflow.com/questions/26643727/python-sqlalchemy-deleting-with-the-session-object
    session().query(Task).filter(Task.g_id == g_id).delete()
    session().query(Group).filter(Group.g_id == g_id).delete()
    ds().commit()
