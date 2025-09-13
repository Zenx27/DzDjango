from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task-list'),
    path('tasks/create/', views.task_create, name='task-create'),
    path('users/', views.users_list, name='users-list'),
    path('users/create/', views.user_create, name='user-create'),
    path('tasks/class/', views.TaskListView.as_view(), name='task-list-class'),
    path('tasks/class/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail-class'),
    path('tasks/meta/', views.TaskMetaView.as_view(), name='task-meta'),
]



