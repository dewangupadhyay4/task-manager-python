from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDelete, CustomAuthToken, register_user


urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name="task_list_create"),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDelete.as_view(), name="ret_update_delete"),
    path('register/', register_user, name='register_user')
]

urlpatterns += [
    path('login/', CustomAuthToken.as_view(), name='api-login'),
]