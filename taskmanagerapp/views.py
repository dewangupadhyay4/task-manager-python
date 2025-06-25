from django.shortcuts import render
from .models import TaskManagerModel
from .serializers import TaskManagerSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework import generics

class TaskListCreateView(generics.ListCreateAPIView):
    queryset=TaskManagerModel.objects.all()
    serializer_class=TaskManagerSerializer

class TaskRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=TaskManagerModel.objects.all()
    serializer_class=TaskManagerSerializer

