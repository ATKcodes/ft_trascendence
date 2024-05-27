from django.urls import path
from . import views

urlpatterns = [
    path("nick/", views.Change_Player, name="change_player"),
    path("winlose/", views.WinLose_count, name="win_lose_count"),
    path("profile_image/", views.update_profile_image, name="profile_image"),
    path("get_profile_image/", views.get_profile_image, name="get_profile_image")
]