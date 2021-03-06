# Generated by Django 4.0 on 2021-12-20 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('posts', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='like',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
