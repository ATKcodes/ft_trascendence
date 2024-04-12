from django.shortcuts import render
from rest_framework import generics, status
from .models import User
from .serializers import UserSerializer, CreateUserSerializer
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView   
# Create your views here.


class UserLog(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer  

class CreateUser(APIView):
    def post(self, request):
        serializer = self.CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            email = serializer.data.get('email')
            queryset = User.objects.filter(username=username, email=email) 
            if queryset.exists():
                User = queryset[0]
                User.username = 'bello'
                User.email = email
                User.save(update_fields=['username', 'email'])
            return Response(UserSerializer(User).data, status=status.HTTP_200_OK)

    
