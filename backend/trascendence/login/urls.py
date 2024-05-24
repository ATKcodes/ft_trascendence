from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.user_list),
    path("users/<int:pk>/", views.user_detail),
    path("register/", views.RegisterView.as_view(), name= "token"),
    path ("login/", views.LoginView.as_view(), name= "login"),
    path ("test/", views.TestView, name= "test"),
    path ("logout/", views.logout, name= "logout"),
    path ("token42/", views.get_42token, name= "token42"),
]
