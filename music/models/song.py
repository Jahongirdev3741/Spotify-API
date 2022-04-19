from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Song(models.Model):
  album=models.ForeignKey('music.Album',on_delete=models.CASCADE)
  title=models.CharField(max_length=256)
  cover=models.URLField(null=True,blank=True)
  source=models.URLField()
  listened=models.IntegerField(default=0)
  likes_count=models.IntegerField(default=0)
  user_of_likes=models.ManyToManyField(User,related_name='likes_of_song')

  def __str__(self) -> str:
    return self.title
