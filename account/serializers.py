from rest_framework import serializers

from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, write_only=True)
    password = serializers.CharField(max_length=20, write_only=True)
    password_2 = serializers.CharField(max_length=64, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_2']

    def validate(self, data):
        if data['password'] != data['password_2']:
            raise serializers.ValidationError('пароли должны совпадать')
        return data

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
