from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

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
    player2 = models.CharField(max_length=250, blank=True)
    score = models.IntegerField(default=0)
    scoreplayer2 = models.IntegerField(default=0)
    date_played = models.DateTimeField(null=True, blank=True)
    date_played_tictactoe = models.DateTimeField(null=True, blank=True)
    matchHistorypong = models.JSONField(default=dict)
    matchHistorytictactoe = models.JSONField(default=dict)
    friend_list = models.ManyToManyField('self', blank=True)


    def save(self, *args, **kwargs):
        if not self.player:
            self.player = self.username
        super().save(*args, **kwargs)