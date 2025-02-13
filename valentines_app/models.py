from django.db import models
from django.utils import timezone

class LoveLetter(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    background_music = models.FileField(upload_to='music/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title
