from django.contrib import admin
from typing import cast

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = cast(tuple, ("email", "first_name", "campaign", "created"))
    list_filter = cast(tuple, ("status", "campaign", "created"))
    search_fields = cast(tuple, ("email", "first_name", "last_name"))
    data_hierarchy = "created"
