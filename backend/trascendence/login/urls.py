from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UserLog.as_view()),
]