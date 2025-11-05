# products/models.py
from django.db import models
from core.models import TimeStampedModel

class Product(TimeStampedModel):
    PLATFORM_CHOICES = [
        ('hotmart', 'Hotmart'),
        ('clickbank', 'ClickBank'),
        ('warriorplus', 'Warrior Plus'),
        ('custom', 'Custom'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    affiliate_url = models.URLField()
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)
