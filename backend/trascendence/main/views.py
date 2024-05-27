from django.shortcuts import render, redirect
from rest_framework import generics, status
from .models import User, CustomToken, CustomTokenAuthentication
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, ProfileImageSerializer
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
from datetime import datetime
from django.utils import timezone


@api_view(['POST'])  
@authentication_classes([SessionAuthentication, CustomTokenAuthentication])
@permission_classes([IsAuthenticated])
def Change_Player(request):
    user = request.user
    user.player = request.data['player']
    if user.player == '':
        return Response({'error': 'Player name cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)
    user.save()
    # Return a success response
    return Response({'player': user.player}, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, CustomTokenAuthentication])
@permission_classes([IsAuthenticated])
def WinLose_count(request):    
    user = request.user
    user.player2 = request.data['player2']
    if request.data['game'] == 'pong':
        if request.data['win'] == 'true':
            user.wins_pong += 1
            user.score = request.data['score']
            user.scoreplayer2 = request.data['scoreplayer2']
            #user.matchHistorypong.append({'game': 'pong', 'win': True, 'score': user.score, 'scoreplayer2': user.scoreplayer2})
        else:
            user.loses_pong += 1
            user.score = request.data['score']
            user.scoreplayer2 = request.data['scoreplayer2']
            #user.matchHistorypong.append({'game': 'pong', 'win': False, 'score': user.score, 'scoreplayer2': user.scoreplayer2})
        user.winrate_pong = user.wins_pong /  (user.wins_pong + user.loses_pong) * 100
        now = timezone.now()
        user.date_played_tictactoe = now
        user.save()
    elif request.data['game'] == 'tictactoe':
        if request.data['win'] == 'true':
            user.wins_tictactoe += 1
            #user.matchHistorytictactoe.append({'game': 'tictactoe', 'win': True})
        else:
            user.loses_tictactoe += 1
            #user.matchHistorytictactoe.append({'game': 'tictactoe', 'win': False})
        user.winrate_tictactoe = user.wins_tictactoe /  (user.wins_tictactoe + user.loses_tictactoe) * 100
        now = timezone.now()
        user.date_played_tictactoe = now
        user.save()
    
    return Response({
        'pong': {
            'wins': user.wins_pong, 
            'loses': user.loses_pong, 
            'winrate': user.winrate_pong, 
        }, 
        'tictactoe': {
            'wins': user.wins_tictactoe, 
            'loses': user.loses_tictactoe, 
            'winrate': user.winrate_tictactoe, 
        }
    }, status=status.HTTP_200_OK)




@api_view(['POST'])
@authentication_classes([SessionAuthentication, CustomTokenAuthentication])
@permission_classes([IsAuthenticated])
def update_profile_image(request):
    serializer = ProfileImageSerializer(data=request.data, instance=request.user)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'response': 'successful'})
    else:
        print(serializer.errors)
        return JsonResponse({'response': 'failed', 'errors': serializer.errors, })



@api_view(['POST'])
@authentication_classes([SessionAuthentication, CustomTokenAuthentication])
@permission_classes([IsAuthenticated])
def get_profile_image(request):
    user = request.user
    if hasattr(user, 'profile_image'):
        return JsonResponse({'profile_image_url': request.build_absolute_uri(user.profile_image.url)})
    else:
        return JsonResponse({'error': 'No profile image found'}, status=404)
