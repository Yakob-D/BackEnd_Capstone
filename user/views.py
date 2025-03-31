from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework import response
# Create your views here.

class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        current_user = authenticate(username=username, password=password)
        if current_user != None:
            token, created = Token.objects.get_or_create(user=current_user)
            return response({'token':token.key})
        else:
            raise ValidationError('Invalid Username or Password') 