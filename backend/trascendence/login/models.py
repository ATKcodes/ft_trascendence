from django.db import models
from django.contrib.auth.models import AbstractUser

class User (AbstractUser):
    username = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250, blank=True)
    wins_pong = models.IntegerField(default=0)
    loses_pong = models.IntegerField(default=0)
    winrate_pong = models.FloatField(default=0)
    wins_tictactoe = models.IntegerField(default=0)
    loses_tictactoe = models.IntegerField(default=0)
    winrate_tictactoe = models.FloatField(default=0)
    player = models.CharField(max_length=250, blank=True)
    friend_list = models.ManyToManyField('self', blank=True)

