from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# Create your views here.

class PostView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    # context_object_name = 'posts'

#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("¡Hola Mundo! La aplicación está funcionando.")