# Generated by Django 4.0.4 on 2022-04-17 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_album_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='listened',
            field=models.IntegerField(default=0),
        ),
    ]
