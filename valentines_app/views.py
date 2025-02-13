from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import LoveLetter, GalleryImage
from .forms import LoveLetterForm, GalleryImageForm

def landing_page(request):
    return render(request, 'valentines_app/landing.html')

class LoveLetterCreateView(CreateView):
    model = LoveLetter
    form_class = LoveLetterForm
    template_name = 'valentines_app/love_letter_form.html'
    success_url = reverse_lazy('valentines_app:love-letter-list')

    def form_valid(self, form):
        messages.success(self.request, 'Your love letter has been created! ❤️')
        return super().form_valid(form)

class LoveLetterListView(ListView):
    model = LoveLetter
    template_name = 'valentines_app/love_letter_list.html'
    context_object_name = 'letters'
    ordering = ['-created_at']

class LoveLetterDetailView(DetailView):
    model = LoveLetter
    template_name = 'valentines_app/love_letter_detail.html'
    context_object_name = 'letter'

class GalleryCreateView(CreateView):
    model = GalleryImage
    form_class = GalleryImageForm
    template_name = 'valentines_app/gallery_form.html'
    success_url = reverse_lazy('valentines_app:gallery')

    def form_valid(self, form):
        messages.success(self.request, 'Your image has been uploaded! 📸')
        return super().form_valid(form)

class GalleryListView(ListView):
    model = GalleryImage
    template_name = 'valentines_app/gallery.html'
    context_object_name = 'images'
    ordering = ['-uploaded_at']
