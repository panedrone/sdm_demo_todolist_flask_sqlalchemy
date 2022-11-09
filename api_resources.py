def add_resources(api):
    from resources.group_resource import GroupResource
    from resources.group_tasks_resource import GroupTasksResource
    from resources.group_list_resource import GroupListResource
    from resources.task_resource import TaskResource

    api.add_resource(GroupListResource, "/groups")
    api.add_resource(GroupResource, "/groups/<int:g_id>")
    api.add_resource(GroupTasksResource, '/groups/<int:g_id>/tasks')
    api.add_resource(TaskResource, '/tasks/<int:t_id>')
