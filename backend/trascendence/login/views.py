from django.shortcuts import render
from rest_framework import generics, status
from .models import User, CustomToken, CustomTokenAuthentication
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.settings import api_settings
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication
from rest_framework import exceptions
import requests
import os
from requests.auth import HTTPBasicAuth
from django.utils.crypto import get_random_string

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"response": "successful"})
    
class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        authenticate_user = authenticate(username=username, password=password)

        if authenticate_user is not None:
            user = User.objects.get(username=username)
            serializer = UserSerializer(user)

            response_data = {
                "user": serializer.data
            }

            token, created = CustomToken.objects.get_or_create(user=user)
            user.status = True
            user.save()
            response = Response({"response": "successful", "token": token.key, "user": response_data})
            return response
        return Response({"detail": "Invalid credentials"})


@api_view(['POST'])  
@authentication_classes([SessionAuthentication, CustomTokenAuthentication])
@permission_classes([IsAuthenticated])
def TestView(request):
    return Response({"detail": "You are authenticfewfated"})

@api_view(['POST'])
@authentication_classes([SessionAuthentication, CustomTokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    user = request.user
    user.status = False
    user.save()
    return Response({"detail": "You are logged out"})



@api_view(['GET'])
def get_42token(request):
    data = {
        'grant_type': 'authorization_code',
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
        'code': request.GET.get('code'),
        'redirect_uri': 'https://localhost:8443/spa-manager.html',
    }
    response = requests.post('https://api.intra.42.fr/oauth/token', json=data)
    if response.status_code == 200:
        response2 = requests.get('https://api.intra.42.fr/v2/me', headers={'Authorization': 'Bearer ' + response.json()['access_token']})
        username = response2.json()['login']
        token42 = response.json()['access_token']
        if not User.objects.filter(username=username).exists():
            serializer = UserSerializer(data={'username': username, 'password': get_random_string(length=40)})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        user = User.objects.get(username=username)
        user.save()
        token, created = CustomToken.objects.get_or_create(user=user, defaults={'key': token42})
        return JsonResponse({'token': token.key, 'user': UserSerializer(user).data})
    else:
        return JsonResponse({'error': 'Failed to get access token'}, status=400)