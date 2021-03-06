# Generated by Django 3.1.5 on 2021-08-20 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat_main', '0022_auto_20210820_1045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='msgsroom',
            old_name='room',
            new_name='to_room',
        ),
        migrations.RemoveField(
            model_name='msgsroom',
            name='user',
        ),
        migrations.AlterField(
            model_name='msgsroom',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_msg_room', to=settings.AUTH_USER_MODEL),
        ),
    ]
