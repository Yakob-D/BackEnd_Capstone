from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long.')
        return password