from django.urls import path
from .views import PostView

urlpatterns = [
    path('', PostView.as_view(), name='post'),
    # Agrega más rutas aquí según necesites
]