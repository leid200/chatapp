# Generated by Django 3.1.5 on 2021-08-24 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_main', '0026_msgsroom_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msgsroom',
            name='msg',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
