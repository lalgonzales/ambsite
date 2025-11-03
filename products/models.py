from django.db import models
from core.models import TimeStampedModel


class Product(TimeStampedModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    hotmart_product_id = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    checkout_url = models.URLField()
    session1_url = models.URLField(blank=True)
    session2_url = models.URLField(blank=True)
    session3_url = models.URLField(blank=True)
    session4_url = models.URLField(blank=True)
    session5_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta(TimeStampedModel.Meta):
        ordering = ["name"]

    def __str__(self):
        return str(self.name)
