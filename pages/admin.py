from django.contrib import admin
from .models import Page, Section


class SectionInline(admin.TabularInline):
    model = Section
    extra = 1
    fields = ["section_type", "order", "data"]


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
        "page_type",
        "is_active",
        "created_at",
        # 'lead_count'
    ]
    list_filter = ["page_type", "is_active", "created_at"]
    search_fields = ["title", "slug"]
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ["is_active"]
    readonly_fields = ["created_at", "updated_at"]
    date_hierarchy = "created_at"

    fieldsets = (
        ("Basic Information", {"fields": ("title", "slug", "page_type", "is_active")}),
        (
            "SEO",
            {"fields": ("meta_title", "meta_description"), "classes": ("collapse",)},
        ),
        ("Dates", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )
    inlines = [SectionInline]
