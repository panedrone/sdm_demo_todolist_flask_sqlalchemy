# sdm_demo_todolist_flask_sqlalchemy
Quick Demo of how to use [SQL DAL Maker](https://github.com/panedrone/sqldalmaker) + Python + Flask-SQLAlchemy.

Front-end is written in Vue.js, SQLite3 is used as database.

![demo-go.png](demo-go.png)

![erd.png](erd.png)

dto.xml
```xml
<dto-class name="sa-Project" ref="groups"/>

<dto-class name="sa-ProjectLi" ref="get_projects.sql"/>

<dto-class name="sa-Task" ref="tasks"/>

<dto-class name="sa-TaskLI" ref="tasks">

    <header><![CDATA[    """
    Task list item
    """
    __table_args__ = {'extend_existing': True}]]></header>

    <field column="t_comments" type="-"/>

</dto-class>
```
ProjectsDao.xml
```xml
<crud dto="sa-Project" table="groups"/>
```
TasksDao.xml
```xml
<crud dto="sa-Task" table="tasks"/>
```
Generated code in action:
```go
def get_all_groups():
    ds = scoped_ds()
    return ProjectsDaoEx(ds).get_all_groups()


def get_project(p_id):
    ds = scoped_ds()
    group = ProjectsDaoEx(ds).read_group(p_id)
    return group


def create_project(p_name):
    ds = scoped_ds()
    group = Project(p_name=p_name)
    ProjectsDaoEx(ds).create_group(group)
    ds.commit()


def update_project(p_id, p_name):
    ds = scoped_ds()
    ProjectsDaoEx(ds).rename(p_id, p_name)
    ds.commit()


def delete_project(p_id):
    ds = scoped_ds()
    ds.delete_by_filter(Task, {"p_id": p_id})
    ProjectsDaoEx(ds).delete_group(p_id)
    ds.commit()
```