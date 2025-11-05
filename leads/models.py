# leads/models.py
from django.db import models
from core.models import TimeStampedModel

class Lead(TimeStampedModel):
    STATUS_CHOICES = [
        ('new', 'Nuevo'),
        ('contacted', 'Contactado'),
        ('converted', 'Convertido'),
        ('unqualified', 'No Calificado'),
    ]

    email = models.EmailField()
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    source_page = models.ForeignKey('pages.Page', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ['email', 'source_page']

    def __str__(self):
        return f"{self.email} - {getattr(self.source_page, 'title', str(self.source_page))}"
