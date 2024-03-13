from rest_framework import serializers
from core.models import Task
from core.account.models import CustomUser
from core.account.serializer import CustomUserSerializer

class TaskSerializer(serializers.ModelSerializer):
    user_detail = CustomUserSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ('id', 'user', 'user_detail', 'title', 'description', 'created_at', 'completed', 'status')
        dept=1