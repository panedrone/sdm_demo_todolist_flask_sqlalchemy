# sdm_demo_todolist_flask_sqlalchemy
Quick Demo of how to use [SQL DAL Maker](https://github.com/panedrone/sqldalmaker) + Python + Flask-SQLAlchemy.

Front-end is written in Vue.js, SQLite3 is used as database.

![demo-go.png](demo-go.png)

dto.xml
```xml
<dto-class name="sa-Project" ref="projects"/>

<dto-class name="sa-ProjectLi" ref="get_projects.sql"/>

<dto-class name="sa-Task" ref="tasks"/>

<dto-class name="sa-TaskLi" ref="tasks">

    <header><![CDATA[    """
    Task list item
    """
    __table_args__ = {'extend_existing': True}]]></header>

    <field column="t_comments" type="-"/>

</dto-class>
```
ProjectsDao.xml
```xml
<crud dto="sa-Project" table="projects"/>
```
TasksDao.xml
```xml
<crud dto="sa-Task" table="tasks"/>
```
Generated code in action:
```go
def get_all_projects():
    ds = scoped_ds()
    return ProjectsDao(ds).get_all_projects()


def get_project(p_id):
    ds = scoped_ds()
    project = ProjectsDao(ds).read_project(p_id)
    return project


def create_project(p_name):
    ds = scoped_ds()
    project = Project(p_name=p_name)
    ProjectsDao(ds).create_project(project)
    ds.commit()


def update_project(p_id, p_name):
    ds = scoped_ds()
    ProjectsDao(ds).rename_project(p_id, p_name)
    ds.commit()


def delete_project(p_id):
    ds = scoped_ds()
    ds.delete_by_filter(Task, {"p_id": p_id})
    ProjectsDao(ds).delete_project(p_id)
    ds.commit()
```