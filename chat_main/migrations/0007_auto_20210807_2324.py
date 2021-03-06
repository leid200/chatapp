# Generated by Django 3.1.5 on 2021-08-07 21:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat_main', '0006_auto_20210807_2323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requested',
            name='user',
        ),
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='userFriends', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='req',
            field=models.ManyToManyField(blank=True, related_name='reqFriends', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Friends',
        ),
        migrations.DeleteModel(
            name='Requested',
        ),
    ]
