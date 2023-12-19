from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('tasks/', views.TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskDetailed.as_view(), name='task-detail'),
    path('tasks/adm/', views.TaskListAdm.as_view(), name='task-list-adm'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
