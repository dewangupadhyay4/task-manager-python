from .models import TaskManagerModel
from rest_framework import serializers

class TaskManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskManagerModel
        fields='__all__'