from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.user_list),
    path("users/<int:pk>/", views.user_detail),
    path("register/", views.RegisterView.as_view(), name= "token"),
    path ("login/", views.LoginView.as_view(), name= "login"),
    path ("test-view/", views.TokenAuthentication.as_view(), name= "test"),
]
