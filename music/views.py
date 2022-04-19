import imp
from rest_framework.viewsets import ModelViewSet
from .models import Artist,Album,Song
from .serializers import ArtistSerializer,AlbumSerializer,SongSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status
from django.db import transaction
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User=get_user_model()

class ArtistViewSet(ModelViewSet):
  serializer_class=ArtistSerializer
  queryset=Artist.objects.all()
  permission_classes=(IsAuthenticated,)

  @action(methods=["GET"],detail=True)
  def albums(self,request,*args,**kwargs):
    artist=self.get_object()
    serializer=ArtistSerializer(artist.album_set.all(),many=True)
    return Response(serializer.data)
  

class AlbumViewSet(ModelViewSet):
  serializer_class=AlbumSerializer
  queryset=Album.objects.all()
  permission_classes=(IsAuthenticated,)

class SongViewSet(ModelViewSet):
  serializer_class=SongSerializer
  filter_backends=[SearchFilter]
  search_fields=['title']
  pagination_class=LimitOffsetPagination
  permission_classes=(IsAuthenticated,)

  def get_queryset(self):
    return Song.objects.all()

  @action(detail=True,methods=["GET"])
  def listen(self,request,*args,**kwargs):
    song=self.get_object()
    with transaction.atomic():
      song.listened += 1
      song.save()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
  @action(detail=False,methods=["GET"])
  def top(self, request,*args,**kwargs):
    song=self.get_queryset()
    song=song.order_by('-listened')[:5]
    serializer=SongSerializer(song,many=True)
    return Response(serializer.data)
  
  @action(detail=True,methods=["POST"])
  def like_and_dislike(self,request,*args,**kwargs):
    song=self.get_object()
    if request.user in song.user_of_likes.all():
      song.likes_count -= 1
      song.user_of_likes.remove(request.user)
      song.save()   
    else:
      song.likes_count += 1
      song.user_of_likes.add(request.user)
      song.save()
    
    return Response(status=status.HTTP_200_OK)


