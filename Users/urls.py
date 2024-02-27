from django.urls import path
from .views import CreateUserView, UpdateUserView, ListUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import LoginJWTView

urlpatterns = [
    path("users/", CreateUserView.as_view()),
    path("users/get/", ListUserView.as_view()),
    path("users/<int:pk>/", UpdateUserView.as_view()),
    path("login/", LoginJWTView.as_view()),  # new
    path("login/refresh/", TokenRefreshView.as_view()),
]
