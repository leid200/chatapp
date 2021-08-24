# Generated by Django 3.1.5 on 2021-08-20 22:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat_main', '0023_auto_20210820_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatgroup',
            name='admins',
            field=models.ManyToManyField(blank=True, related_name='admins', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chatgroup',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='usersIn', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='msgsroom',
            name='to_room',
            field=models.ManyToManyField(blank=True, related_name='group_msgs', to='chat_main.ChatGroup'),
        ),
    ]
