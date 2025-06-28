from django.shortcuts import render
from .models import TaskManagerModel
from .serializers import TaskManagerSerializer, RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class TaskListCreateView(generics.ListCreateAPIView):
    queryset=TaskManagerModel.objects.all()
    serializer_class=TaskManagerSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return TaskManagerModel.objects.filter(user=self.request.user)
    
    def perfom_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=TaskManagerModel.objects.all()
    serializer_class=TaskManagerSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return TaskManagerModel.objects.filter(user=self.request.user)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response= super().post(request, *args, **kwargs)
        token=Token.objects.get(key=response.data['token'])
        return Response({
            'token':token.key,
            'user_id':token.user_id,
            'username':token.user.username

        })
    
@api_view(['POST'])
def register_user(request):
    serializer=RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)