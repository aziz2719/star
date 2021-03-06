# Generated by Django 4.0 on 2021-12-20 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('image', models.FileField(blank=True, null=True, upload_to='post_images', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
                'ordering': ('-id',),
            },
        ),
    ]
