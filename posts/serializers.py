from rest_framework import serializers
from posts import models
from posts import services as likes_services
from django.contrib.auth import get_user_model


User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = models.Post
        fields = ('id', 'user', 'title', 'text', 'date', 'image', 'is_fan', 'total_likes')

    def create(self, validated_data):
        user = self.context.get('request').user
        post = models.Post.objects.create(user=user, **validated_data)
        return post

    def get_is_fan(self, obj) -> bool:
        """Проверяет, лайкнул ли `request.user` твит (`obj`).
        """
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = ('__all__')


class FanSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'email',
            'full_name',
        )

    def get_full_name(self, obj):
        return obj.get_full_name()





