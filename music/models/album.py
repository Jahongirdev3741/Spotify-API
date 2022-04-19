from django.db import models

class Album(models.Model):
  artist=models.ForeignKey('music.Artist',on_delete=models.CASCADE)
  name=models.CharField(max_length=256)
  cover=models.URLField(null=True, blank=True)

  def __str__(self) -> str:
    return self.name