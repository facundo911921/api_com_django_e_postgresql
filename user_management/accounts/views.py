from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.hashers import make_password
from .models import CustomUser
from .serializers import UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(password=make_password(serializer.validated_data['password']))
