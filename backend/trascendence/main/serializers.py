from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework.serializers import ModelSerializer
from django import forms


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None) 
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        return instance

class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['profile_image']


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'profile_image', 'player', 'wins_pong', 'loses_pong', 'winrate_pong', 'wins_tictactoe', 'loses_tictactoe', 'draw_tictactoe', 'winrate_tictactoe', 'status', 'matchistory_pong', 'matchistory_tictactoe']
