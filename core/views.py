from django.shortcuts import render

from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Task, User
from .serializers import (
    TaskCreateUpdateSerializer,
    TaskSerializer,
    UserCreateSerializer,
    UserSerializer,
)


# Traditional Django Views
def home(request):
    """Simple home page view"""
    context = {
        "title": "Django API Boilerplate",
        "users_count": User.objects.count(),
        "tasks_count": Task.objects.count(),
    }
    return render(request, "core/home.html", context)


def tasks_list(request):
    """List all tasks view"""
    tasks = Task.objects.select_related("created_by").all()
    context = {"tasks": tasks}
    return render(request, "core/tasks.html", context)


# API Views
class UserListCreateAPIView(generics.ListCreateAPIView):
    """List all users or create a new user"""

    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserCreateSerializer
        return UserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        return [permissions.IsAuthenticated()]


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a user"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskListCreateAPIView(generics.ListCreateAPIView):
    """List all tasks or create a new task"""

    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.select_related("created_by").all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return TaskCreateUpdateSerializer
        return TaskSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a task"""

    queryset = Task.objects.select_related("created_by").all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return TaskCreateUpdateSerializer
        return TaskSerializer


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def api_stats(request):
    """Get API statistics"""
    stats = {
        "total_users": User.objects.count(),
        "total_tasks": Task.objects.count(),
        "completed_tasks": Task.objects.filter(completed=True).count(),
        "current_user": request.user.username,
    }
    return Response(stats)
