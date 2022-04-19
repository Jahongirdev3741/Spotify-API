from django.db import models
from django.contrib.auth import get_user_model
from .song import Song

User=get_user_model()

class Comment(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  song=models.ForeignKey(Song,on_delete=models.CASCADE)
  text=models.TextField(max_length=1000)
  create_at=models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return self.text