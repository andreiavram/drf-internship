from rest_framework import serializers

from todolist.models import TaskItem, Project


class TaskItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = ("id", "title", "due_date", "creation_date", "description", "owner", "project", "cost", "last_update_date", "status")


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "name", "owner", "task_count")

    task_count = serializers.SerializerMethodField(read_only=True)

    def get_task_count(self, instance):
        return TaskItem.objects.filter(project=instance).count()
