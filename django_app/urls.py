from django.urls import path
from .views import *
# Agrega esta importación en la parte superior del archivo
from django_app.views import PostDetailView  # ← Importa la vista
from .views import PostDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # ← Ahora funcionará
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)