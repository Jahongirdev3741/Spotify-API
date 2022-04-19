from turtle import st
from rest_framework.serializers import ModelSerializer
from .models import Artist,Album,Song
from rest_framework.exceptions import ValidationError

class ArtistSerializer(ModelSerializer):
  class Meta:
    model=Artist
    fields=('id','name','picture',)

class AlbumSerializer(ModelSerializer):
  class Meta:
    model=Album
    fields=('id','name','cover','artist')

class SongSerializer(ModelSerializer):
  class Meta:
    model=Song
    fields=('id','title','cover','source','album','listened','likes_count')
  
  def validate_source(self, value:str):

    if not value.endswith('.mp3'):
      raise ValidationError(detail="Mp3 File is required")

    return value