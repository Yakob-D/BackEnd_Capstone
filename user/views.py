from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({"error": "Username and password are required"})  # Fixed usage
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})  # Fixed usage
        else:
            raise ValidationError("Invalid username or password")

class LogoutView(APIView):
    def post(self, request):
        token_key = request.headers.get('Authorization')
        if not token_key:
            return Response({"error": "Token required"}, status=status.HTTP_400_BAD_REQUEST)
        if not token_key.startswith('Token '):
            return Response({"error": "Invalid token format"}, status=status.HTTP_400_BAD_REQUEST)
        
        key = token_key.split(' ')[1]
        try:
            token = Token.objects.get(key=key)
            token.delete()
            return Response({"message": "Success"}, status=status.HTTP_200_OK)  # Fixed
        except Token.DoesNotExist:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)