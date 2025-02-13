from django.contrib import admin
from .models import LoveLetter, GalleryImage

@admin.register(LoveLetter)
class LoveLetterAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title', 'description')
    list_filter = ('uploaded_at',)
    date_hierarchy = 'uploaded_at'
    ordering = ('-uploaded_at',)
