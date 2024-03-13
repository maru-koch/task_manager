from django.urls import path, include
from core.views import TaskDetailView, TasksView, TasksAnalytics
urlpatterns = [
    path('account/', include('core.account.urls')),
    path('tasks', TasksView.as_view(), name='tasks'),
    path('tasks/<uuid:pk>', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/analytics', TasksAnalytics.as_view(), name='tasks-analytics')
]