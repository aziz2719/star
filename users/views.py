from rest_framework_simplejwt.views import (
    TokenObtainPairView as SimpleTokenObtainPairView,
)
from rest_framework import viewsets
from users import serializers
from users import models


class TokenObtainPairView(SimpleTokenObtainPairView):
    serializer_class = serializers.TokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_serializer_class(self):
        if self.action in ["create"]:
            return serializers.UserCreateSerializer
        return self.serializer_class
