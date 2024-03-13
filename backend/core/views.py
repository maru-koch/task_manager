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

    # def get_queryset(self):
    #     """Returns only the login user's tasks 
    #     if the person is not an admin."""
    #     if self.request.user.is_authenticated:
    #         if self.request.user.is_admin:
    #             return Task.objects.all()
    #         return Task.objects.filter(user=self.request.user)

class TaskDetailView(RetrieveUpdateDestroyAPIView, LoginRequiredMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TasksAnalytics(APIView, LoginRequiredMixin):
    """Retrieves the tasks analytics. """
    def get(self, request, format='json'):
        user = request.user
        # tasks = Task.objects.all() if user.is_admin else Task.objects.filter(user=request.user)
        tasks = Task.objects.all()
        return Response({
            'total_tasks':tasks.count(),
            'completed_tasks':tasks.filter(status="completed").count(),
            'pending_tasks':tasks.filter(status="todo").count(),
            'in_progress_tasks':tasks.filter(status="in progress").count()
        })