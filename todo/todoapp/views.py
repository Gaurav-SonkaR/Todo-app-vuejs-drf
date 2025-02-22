from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

def index(request):
    return HttpResponse("Hello, You're at the todoapp index.")

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET','PUT', 'PATCH'])
def taskUpdate(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'GET':
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data, status=200)
    elif request.method == 'PUT':
        serializer = TaskSerializer(instance=task, data=request.data)
    elif request.method == 'PATCH':
        serializer = TaskSerializer(instance=task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def taskDelete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return Response('Item succsesfully delete!')