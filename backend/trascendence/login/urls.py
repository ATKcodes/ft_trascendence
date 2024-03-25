from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<str:extra_path>", views.index2)
]