from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("thank-you", views.thank_you),
    path("<str:extra_path>", views.index2)
]
