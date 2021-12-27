from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


User = get_user_model()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(default=0, null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, null=True, blank=True)


class Post(models.Model):
    user = models.ForeignKey(User, models.CASCADE, related_name='owner', null=True, blank=True)
    title = models.CharField(verbose_name='Описание', max_length=255, blank=True, null=True)
    text = models.TextField(verbose_name='Текст', blank=True, null=True)
    date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    image = models.FileField(verbose_name='Фото', upload_to = 'post_images', blank=True, null=True)
    likes = GenericRelation(Like)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-id',)

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()
