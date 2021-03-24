from django.shortcuts import render
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Hero

from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message':"Got some data!","data":request.data})
    return Response({'message':'Hello, world!'})


class ListUsers(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self,request,format=None):
        
        username = [user.username for user in User.objects.all()]
        return Response(username)

class HeroViewSet(viewsets.ModelViewSet):
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
