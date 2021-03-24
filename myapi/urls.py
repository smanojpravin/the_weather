from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import HeroViewSet
from rest_framework import routers
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'heroes',HeroViewSet)



urlpatterns = [
    path('',include(router.urls)),
    path('api-token-auth/',views.obtain_auth_token,name='api-token-auth'),
]