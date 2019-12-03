from rest_framework import viewsets
from .Serializers import TaskSerializer
from .models import Task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.Objects.all()
    serializer_class = TaskSerializer
