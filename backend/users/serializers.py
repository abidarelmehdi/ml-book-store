from rest_framework import serializers
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "profile_picture",
            "gender",
            "email",
            "first_name",
            "last_name",
            "birthday",
            "twitter",
            "linkedin",
        )
