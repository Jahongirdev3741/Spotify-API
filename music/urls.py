from django.urls import path,include
from .views import ArtistViewSet,AlbumViewSet,SongViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('artist',ArtistViewSet,'artist')
router.register('album',AlbumViewSet,'album')
router.register('song',SongViewSet,'song')

urlpatterns=[
  path('',include(router.urls))
]