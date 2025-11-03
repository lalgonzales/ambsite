from itertools import count
import email
from django.db import models
from core.models import TimeStampedModel
from campaigns.models import Campaign


class Lead(TimeStampedModel):
    STATUS_CHOICES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("qualified", "Qualified"),
        ("converted", "Converted"),
        ("unqualified", "Unqualified"),
    ]

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)
    campaign = models.ForeignKey(
        Campaign, on_delete=models.SET_NULL, null=True, related_name="leads"
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    notes = models.TextField(blank=True)

    class Meta(TimeStampedModel.Meta):
        ordering = ["-created"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}>"
