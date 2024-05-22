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



@api_view(['POST'])  
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def Change_Player(request):
    # Get the user from the request
    user = request.user
    # Get the new player value from the request data
    # Update the player field of the user
    user.player = "valerio"
    user.save()
    # Return a success response
    return Response({'player': user.player}, status=status.HTTP_200_OK)