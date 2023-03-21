# sdm_demo_todolist_flask_sqlalchemy
Quick Demo of how to use [SQL DAL Maker](https://github.com/panedrone/sqldalmaker) + Python + Flask-SQLAlchemy.

Front-end is written in Vue.js, SQLite3 is used as database.

![demo-go.png](demo-go.png)

![erd.png](erd.png)

dto.xml
```xml
<dto-class name="sa-Group" ref="groups"/>

<dto-class name="sa-GroupLi" ref="get_groups.sql"/>

<dto-class name="sa-Task" ref="tasks"/>

<dto-class name="sa-TaskLI" ref="tasks">

    <header><![CDATA[    """
    Task list item
    """
    __table_args__ = {'extend_existing': True}]]></header>

    <field column="t_comments" type="-"/>

</dto-class>
```
GroupsDao.xml
```xml
<crud dto="sa-Group" table="groups"/>
```
TasksDao.xml
```xml
<crud dto="sa-Task" table="tasks"/>
```
Generated code in action:
```go
def get_all_groups():
    ds = scoped_ds()
    return GroupsDaoEx(ds).get_all_groups()


def get_group(g_id):
    ds = scoped_ds()
    group = GroupsDaoEx(ds).read_group(g_id)
    return group


def create_group(g_name):
    ds = scoped_ds()
    group = Group(g_name=g_name)
    GroupsDaoEx(ds).create_group(group)
    ds.commit()


def update_group(g_id, g_name):
    ds = scoped_ds()
    GroupsDaoEx(ds).rename(g_id, g_name)
    ds.commit()


def delete_group(g_id):
    ds = scoped_ds()
    ds.delete_by_filter(Task, {"g_id": g_id})
    rows_deleted = GroupsDaoEx(ds).delete_group(g_id)
    print(f"rows_deleted: {rows_deleted}")
    ds.commit()
```