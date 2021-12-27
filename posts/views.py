from rest_framework.viewsets import ModelViewSet
from posts import models
from posts import serializers
from posts.mixins import LikedMixin
from rest_framework.response import Response
from rest_framework import status


class PostView(LikedMixin, ModelViewSet):
    queryset = models.Post.objects.order_by('-date')
    serializer_class = serializers.PostSerializer


class LikeView(ModelViewSet):
    queryset = models.Like.objects.order_by('-date')
    serializer_class = serializers.LikeSerializer
