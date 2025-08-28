from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):  # ← El modelo debe estar AQUÍ, en models.py
    title = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title