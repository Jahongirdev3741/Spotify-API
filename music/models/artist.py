from django.db import models

class Artist(models.Model):
  name=models.CharField(max_length=256)
  picture=models.URLField(null=True,blank=True)

  def __str__(self) -> str:
    return self.name