from rest_framework import serializers
from core.models import Task
from core.account.serializer import CustomUserSerializer

class TaskSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
 
    class Meta:
        model = Task
        fields = '__all__'
