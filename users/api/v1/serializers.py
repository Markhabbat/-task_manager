from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.models import User, Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = (
            "id",
            "name",
            "description",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "role",
        )

    def validate(self, attrs):
        if password := attrs.get('password', None):
            attrs['password'] = make_password(password)
        return attrs
