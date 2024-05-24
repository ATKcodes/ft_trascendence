from django.shortcuts import render
from rest_framework import generics, status
from .models import User
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
from requests.auth import HTTPBasicAuth

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)

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

            token, created = Token.objects.get_or_create(user=user)
            response = Response({"response": "successful", "token": token.key})
            return response
        return Response({"detail": "Invalid credentials"})


@api_view(['POST'])  
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def TestView(request):
    return Response({"detail": "You are authenticfewfated"})

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    return Response({"detail": "You are logged out"})



def get_42token(request):
    data = {
        'grant_type': 'authorization_code',
        'client_id': 'u-s4t2ud-a8a7afc615b7c393b1a141953798a4f72bfd49e80f8464df3f2ac1838557eefe',
        'client_secret': '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',
        'code': 'fee85417f63d998c07a584402fa84f4e599b09194fa437a9dab95bc9aff18f27',
        'redirect_uri': 'http://127.0.0.1:8080/main-page.html',
    }
    response = requests.post('https://api.intra.42.fr/oauth/token', data=data)
    if response.status_code == 200:
        response2 = requests.get('https://api.intra.42.fr/v2/me', headers={'Authorization': 'Bearer ' + response.json()['access_token']})
        username = response2.json()['login']
        if not User.objects.filter(username=username).exists():
            serializer = UserSerializer(data={'username': username})
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return JsonResponse({'access_token': response.json()['access_token']})
    else:
        return JsonResponse({'error': 'Failed to get access token'}, status=400)