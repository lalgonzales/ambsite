from django.contrib import admin
from .models import Campaign, LandingPage


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("name", "description")
    date_hierarchy = "created_at"


@admin.register(LandingPage)
class LandingPageAdmin(admin.ModelAdmin):
    list_display = ("title", "campaign", "view_count", "conversion_count", "created_at")
    list_filter = ("campaign", "template", "created_at")
    search_fields = ("title", "slug")
    date_hierarchy = "created_at"
    prepopulated_fields = {"slug": ("title",)}
