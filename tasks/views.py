from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_fields = ['done']

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Add appropriate permissions if needed

class TaskDetailview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]