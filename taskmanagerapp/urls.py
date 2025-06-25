from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDelete

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name="task_list_create"),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDelete.as_view(), name="ret_update_delete")
]