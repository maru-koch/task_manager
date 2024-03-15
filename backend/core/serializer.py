from rest_framework import serializers
from core.models import Task
from core.account.models import CustomUser
from core.account.serializer import CustomUserSerializer

class TaskSerializer(serializers.ModelSerializer):
    user  = CustomUserSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'description', 'created_at', 'completed', 'status')
        dept=1

    def create(self, validated_data):
        user = self.context['request'].user
        task = Task(user=user, **validated_data)
        task.save()
        return task