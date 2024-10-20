from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from django import forms
from rest_framework.serializers import ModelSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "profile_image",
            "player",
            "password",
            "friendlist",
            "wins_pong",
            "loses_pong",
            "winrate_pong",
            "wins_tictactoe",
            "loses_tictactoe",
            "winrate_tictactoe",
            "matchistory_pong",
            "matchistory_tictactoe",
            "language",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["profile_image"]
