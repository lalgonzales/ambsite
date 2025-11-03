from _operator import is_
from random import choices
from secrets import choice
from django.db import models
from core.models import TimeStampedModel


class Campaign(TimeStampedModel):
    name = models.CharField(max_length=200)
    source = models.CharField(
        max_length=50,
        choices=[
            ("facebook", "Facebook Ads"),
            ("google", "Google Ads"),
            ("organic", "Organic Search"),
            ("email", "Email Marketing"),
        ],
    )
    utm_source = models.CharField(max_length=100, blank=True)
    utm_medium = models.CharField(max_length=100, blank=True)
    utm_campaign = models.CharField(max_length=100, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
