from django.db import models


class LeadWebinar(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    webinar = models.CharField(max_length=100, default="Webinar Principal")

    def __str__(self):
        return f"{self.nombre} - {self.email}"
