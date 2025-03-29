from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsTaskOwner

class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        tasks = cache.get('tasks')
        if not tasks:
            tasks = self.get_queryset()
            cache.set('tasks', tasks)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        cache.delete('tasks')
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsTaskOwner]

    def get(self, request, *args, **kwargs):
        task = cache.get(f'task_{kwargs["pk"]}')
        if not task:
            task = self.get_object()
            cache.set(f'task_{kwargs["pk"]}', task)
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = self.get_serializer(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        cache.set(f'task_{kwargs["pk"]}', task)
        cache.delete('tasks')
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        task = self.get_object()
        self.perform_destroy(task)
        cache.delete(f'task_{kwargs["pk"]}')
        cache.delete('tasks')
        return Response(status=status.HTTP_204_NO_CONTENT)
