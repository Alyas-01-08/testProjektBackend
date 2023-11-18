from django.shortcuts import render
from rest_framework import viewsets

from task.models import Task
from task.serializers import TaskSerializer


class TasksVIEWSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
