# Generated by Django 4.0.4 on 2022-04-17 16:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0004_song_listened'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='likes_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='song',
            name='user_of_likes',
            field=models.ManyToManyField(related_name='likes_of_song', to=settings.AUTH_USER_MODEL),
        ),
    ]