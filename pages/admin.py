from django.contrib import admin
from typing import cast

from .models import (
    PageType,
    ModularLandingPage,
    Item,
    PageItem,
)


class PageItemInline(admin.TabularInline):
    model = PageItem
    extra = 1


@admin.register(PageType)
class PageTypeAdmin(admin.ModelAdmin):
    list_display = cast(tuple, ("name", "code", "is_active"))
    list_filter = cast(tuple, ("code", "is_active"))


@admin.register(ModularLandingPage)
class ModularLandingPageAdmin(admin.ModelAdmin):
    list_display = cast(tuple, ("name", "slug", "page_type", "campaign", "is_active"))
    list_filter = cast(tuple, ("is_active", "campaign", "page_type"))
    inlines = cast(tuple, (PageItemInline,))
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "item_type", "is_active")
    list_filter = ("item_type", "is_active")
    search_fields = ("name",)
