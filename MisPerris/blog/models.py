from django.db import models
from django.utils import timezone

class Rescatado(models.Model):
    foto = models.ImageField(default='default.png', blank=True)
    nombre = models.CharField(max_length=30)
    raza = models.CharField(max_length=30)
    descripcion = models.TextField()
    estado = models.CharField(max_length=30)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre
