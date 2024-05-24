from django.urls import path
from . import views

urlpatterns = [
    path("nick/", views.Change_Player, name="change_player"),
    path("winlose/", views.WinLose_count, name="win_lose_count")
]