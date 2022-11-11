"""sunhack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
from . import views

urlpatterns = [
    path('', UserApi.as_view(), name="create_user"),
    path('update/', UpdateCurrentUserApi.as_view(), name="update_user"),
    path('myinfo/', GetCurrentUserInfoAPI.as_view(), name="get_user"),
    path("token/", CreateTokenView.as_view(), name="create_token"),
    path("monuments/", CreateMonuments.as_view(), name="create_monuments"),
    path('logout/',UserLogoutApi.as_view(),name='logout'),
]
