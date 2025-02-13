from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'valentines_app'

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('letter/create/', views.LoveLetterCreateView.as_view(), name='love-letter-create'),
    path('letters/', views.LoveLetterListView.as_view(), name='love-letter-list'),
    path('letter/<int:pk>/', views.LoveLetterDetailView.as_view(), name='love-letter-detail'),
    path('gallery/upload/', views.GalleryCreateView.as_view(), name='gallery-upload'),
    path('gallery/', views.GalleryListView.as_view(), name='gallery'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 