from rest_framework.generics import (
    ListCreateAPIView, 
    RetrieveUpdateDestroyAPIView)
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from serializer import TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from models import Task


class TasksView(ListCreateAPIView, LoginRequiredMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        if not self.request.user.is_admin:
            return Task.objects.filter(user=self.request.user)

class TaskDetailView(RetrieveUpdateDestroyAPIView, LoginRequiredMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAnalytics(APIView):
    """Retrieves the tasks analytics. """
    def get(self, request, format=None):
        total_tasks = Task.objects.all().count()
        completed_tasks = Task.objects.filter(completed=True).count()
        pending_tasks = Task.objects.filter(completed=False).count()
        return Response({
            'total_tasks':total_tasks,
            'completed_tasks':completed_tasks,
            'pending_tasks':pending_tasks
        })