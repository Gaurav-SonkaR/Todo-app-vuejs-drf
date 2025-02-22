from django.urls import path
from .views import *

urlpatterns = [
    path('task-list/', taskList, name='task-list'),
    path('task-create/', taskCreate, name='task-create'),
    path('task-update/<int:id>/', taskUpdate, name='task-update'),
    path('task-detail/<int:id>/', taskUpdate, name='task-detail'),
    path('task-delete/<int:id>/', taskDelete, name='task-delete'),
]