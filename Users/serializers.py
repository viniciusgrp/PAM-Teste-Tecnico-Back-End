from rest_framework import serializers
from .models import User
from Boletim.models import Relatorio
from Boletim.serializers import RelatorioSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser

        return token


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id","username","email","password","is_professor","is_active", "is_superuser", "name", "parent_name", "phone", "parent_phone"]
        read_only_fields = ["id"]
        extra_kwargs = {"password": {"write_only": True}}
        depth = 1


    def create(self, validated_data: dict) -> User:
        if validated_data["is_professor"]:
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.set_password(validated_data["password"])

        instance.save()

        return instance
