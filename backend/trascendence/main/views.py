from django.shortcuts import render, redirect
from rest_framework import generics, status
from .models import User, CustomToken, CustomTokenAuthentication
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, ProfileImageSerializer
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
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


@api_view(["POST"])
@authentication_classes([SessionAuthentication, CustomTokenAuthentication])
@permission_classes([IsAuthenticated])
def Change_Player(request):
    user = request.user
    user.player = request.data["player"]
    if user.player == "":
        return Response(
            {"error": "Player name cannot be empty"}, status=status.HTTP_400_BAD_REQUEST
        )
    user.save()
    # Return a success response
    return Response({"player": user.player}, status=status.HTTP_200_OK)


@api_view(["POST"])
@authentication_classes([SessionAuthentication, CustomTokenAuthentication])
@permission_classes([IsAuthenticated])
def WinLose_pong(request):
    user = request.user
    user.player2 = request.data["player2"]
    if request.data["game"] == "pong":
        if request.data["win"] == "true":
            user.wins_pong += 1
            user.score = request.data["score"]
            user.scoreplayer2 = request.data["scoreplayer2"]
            user.matchHistorypong.append(
                {
                    "game": "pong",
                    "win": "true",
                    "score": user.score,
                    "scoreplayer2": user.scoreplayer2,
                }
            )
        else:
            user.loses_pong += 1
            user.score = request.data["score"]
            user.scoreplayer2 = request.data["scoreplayer2"]
            user.matchHistorypong.append(
                {
                    "game": "pong",
                    "win": "false",
                    "score": user.score,
                    "scoreplayer2": user.scoreplayer2,
                }
            )
        user.winrate_pong = user.wins_pong / (user.wins_pong + user.loses_pong) * 100
        now = timezone.now()
        user.date_played = now
        user.save()
        return Response(
            {
                "pong": {
                    "wins": user.wins_pong,
                    "loses": user.loses_pong,
                    "winrate": user.winrate_pong,
                    "matchHistory": user.matchHistorypong,
                }
            },
            status=status.HTTP_200_OK,
        )


@api_view(["POST"])
@authentication_classes([SessionAuthentication, CustomTokenAuthentication])
@permission_classes([IsAuthenticated])
def WinLose_tictac(request):
    user = request.user
    user.player2 = request.data["player2"]
    if request.data["game"] == "tictactoe":
        if request.data["win"] == "true":
            user.wins_tictactoe += 1
            user.matchHistorytictactoe.append({"game": "tictactoe", "win": "true", "player2": user.player2})
        elif request.data["win"] == "false":
            user.loses_tictactoe += 1
            user.matchHistorytictactoe.append({"game": "tictactoe", "win": "false", "player2": user.player2})
        else:
            user.draw_tictactoe += 1
            user.matchHistorytictactoe.append({"game": "tictactoe", "win": "draw", "player2": user.player2})
        user.winrate_tictactoe = (
            user.wins_tictactoe / (user.wins_tictactoe + user.loses_tictactoe) * 100
        )
        now = timezone.now()
        user.date_played_tictactoe = now
        user.save()

    return Response(
        {
            "tictactoe": {
                "wins": user.wins_tictactoe,
                "loses": user.loses_tictactoe,
                "winrate": user.winrate_tictactoe,
                "draws": user.draw_tictactoe,
                "matchHistory": user.matchHistorytictactoe,
            }
        },
        status=status.HTTP_200_OK,
    )

@api_view(["POST"])
@authentication_classes([SessionAuthentication, CustomTokenAuthentication])
@permission_classes([IsAuthenticated])
def update_profile_image(request):
    if request.method == 'POST':
        file = request.FILES['image']
        file_name = default_storage.save(file.name, file)
        file_url = default_storage.url(file_name)
    
    return JsonResponse({'file_url': file_url})


@api_view(["POST"])
@authentication_classes([SessionAuthentication, CustomTokenAuthentication])
@permission_classes([IsAuthenticated])
def get_profile_image(request):
    user = request.user
    if hasattr(user, "profile_image"):
        return JsonResponse(
            {"profile_image_url": request.build_absolute_uri(user.profile_image.url)}
        )
    else:
        return JsonResponse({"error": "No profile image found"}, status=404)


@api_view(["POST"])
@authentication_classes([SessionAuthentication, CustomTokenAuthentication])
@permission_classes([IsAuthenticated])
def add_friend(request):
    user = request.user
    try:
        friend_username = request.data["friend_username"]
        if not friend_username:
            return HttpResponseBadRequest("friend_username is required")
        if friend_username == user.username:
            return JsonResponse(
                {"error": "You cannot add yourself as a friend"}, status=400
            )
        new_friend = User.objects.get(username=friend_username)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)
    user.add_friend(new_friend)
    return JsonResponse({"response": "successful friend added"}, status=200)


@api_view(["GET"])
@authentication_classes([SessionAuthentication, CustomTokenAuthentication])
@permission_classes([IsAuthenticated])
def get_friends(request):
    user = request.user
    friends = user.get_friends()
    friends_list = [
        {"username": friend.username, "status": friend.status} for friend in friends
    ]
    return JsonResponse({"friends": friends_list}, status=200)


@api_view(["DELETE"])
@authentication_classes([SessionAuthentication, CustomTokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_user(request):
    user = request.user
    user.delete()
    return Response({"message": "User deleted successfully"}, status=status.HTTP_200_OK)
