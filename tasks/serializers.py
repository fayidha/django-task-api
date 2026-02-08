from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'status', 'created_at', 'updated_at']

    def validate_status(self, value):
        valid_choices = ['Pending', 'Completed']
        if value not in valid_choices:
            raise serializers.ValidationError("Status must be 'Pending' or 'Completed'")
        return value

