from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "source", "status", "created_at")
    list_filter = ("status", "source", "created_at")
    search_fields = ("name", "email", "phone")
    date_hierarchy = "created_at"

    fieldsets = (
        ("Contact Information", {"fields": ("name", "email", "phone")}),
        ("Tracking", {"fields": ("source", "campaign", "landing_page", "status")}),
        ("UTM Parameters", {"fields": ("utm_source", "utm_medium", "utm_campaign")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

    readonly_fields = ("created_at", "updated_at")
