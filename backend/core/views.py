from rest_framework.generics import (
    ListCreateAPIView, 
    RetrieveUpdateDestroyAPIView)
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from core.serializer import TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from core.models import Task


class TasksView(ListCreateAPIView, LoginRequiredMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        """Returns only the login user's tasks 
        if the person is not an admin."""
        if not self.request.user.is_admin:
            return Task.objects.filter(user=self.request.user)

class TaskDetailView(RetrieveUpdateDestroyAPIView, LoginRequiredMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TasksAnalytics(APIView):
    """Retrieves the tasks analytics. """
    def get(self, request, format=None):
        tasks = Task.objects.all(user=request.user)
        return Response({
            'total_tasks':tasks.total,
            'completed_tasks':tasks.completed,
            'pending_tasks':tasks.pending
        })