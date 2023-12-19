from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        task = Task(**validated_data)
        task.usertask = self.context['request'].user
        task.save()
        return task
    
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['usertask']