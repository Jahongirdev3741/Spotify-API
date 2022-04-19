from django.contrib import admin
from .models import Artist,Album,Song,Comment
from import_export.admin import ImportExportActionModelAdmin

@admin.register(Artist)
class ArtistAdmin(ImportExportActionModelAdmin):
  search_fields=('name',)
  list_display=('name','picture')


@admin.register(Album)
class AlbumAdmin(ImportExportActionModelAdmin):
  search_fields=('name',)
  list_display=('name','cover')
  autocomplete_fields=('artist',)
  list_filter=("name",)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
  search_fields=('title',)
  list_display=('title','source')
  autocomplete_fields=('album',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display=('user','song','text')
  autocomplete_fields=('user','song',)