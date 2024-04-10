from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UserViewSet.as_view()),
    path("", views.index),
    path("thank-you", views.thank_you),
]