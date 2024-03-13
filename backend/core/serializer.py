from rest_framework import serializers
from models import Task
from core.account.serializer import CustomUserSerializer

class TaskSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    total_tasks = serializers.SerializerMethodField()
    completed_tasks = serializers.SerializerMethodField()
    pending_tasks = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'

    def get_total_tasks(self, obj):
        return obj.total_tasks