from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post  # ← Importar el modelo CORRECTAMENTE

# Create your views here.

class PostView(ListView):
    model = Post  # ← Ahora Post está importado desde models.py
    template_name = 'home.html'
    # context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.all().select_related('user')[:5]

class PostDetailView(DetailView):
    model = Post  # ← Usa el modelo importado
    template_name = 'post_detail.html'
    #  context_object_name = 'posts'