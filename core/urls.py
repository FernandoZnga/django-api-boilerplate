from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    # Traditional Django views
    path("", views.home, name="home"),
    path("tasks/", views.tasks_list, name="tasks_list"),
    # API endpoints
    path("api/users/", views.UserListCreateAPIView.as_view(), name="api_users"),
    path(
        "api/users/<int:pk>/", views.UserDetailAPIView.as_view(), name="api_user_detail"
    ),
    path("api/tasks/", views.TaskListCreateAPIView.as_view(), name="api_tasks"),
    path(
        "api/tasks/<int:pk>/", views.TaskDetailAPIView.as_view(), name="api_task_detail"
    ),
    path("api/stats/", views.api_stats, name="api_stats"),
]
