from django.urls import path, include
from views import TaskDetailView, TasksView, TasksAnalytics
urlpatterns = [
    path('account', include('account.urls')),
    path('tasks', TasksView.as_view(), name='create-task'),
    path('tasks/<id:uuid>', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/analytics', TasksAnalytics.as_view(), name='task-analytics')
]