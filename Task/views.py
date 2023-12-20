from rest_framework import generics, permissions, filters
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, template_name='index.html')

class TaskList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer
    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous:
            return Task.objects.filter(usertask=user)
        return Task.objects.none()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']

class TaskDetailed(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer
    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous:
            if user.is_superuser:
                return Task.objects.all()
            return Task.objects.filter(usertask=user)
        return Task.objects.none()

class TaskListAdm(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']