from django.contrib import admin
from posts import models


admin.site.register(models.Post)
admin.site.register(models.Like)