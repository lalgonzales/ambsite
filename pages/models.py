from django.db import models
from core.models import TimeStampedModel


class PageType(TimeStampedModel):
    """Defines types of pages (landing, sales, product) with default sections and item slots."""

    PAGE_TYPES = [
        ("landing", "Landing Page"),
        ("sales", "Sales Page"),
        ("product", "Product Page"),
    ]

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, choices=PAGE_TYPES, unique=True)
    description = models.TextField(blank=True)
    section_definitions = models.JSONField(
        blank=True,
        null=True,
        help_text='JSON like {"hero": {"items": ["text1", "text2", "video", "cta"]}, "benefits": {"items": ["item1", "item2", ..., "item6"]}}',
    )
    is_active = models.BooleanField(default=True)

    class Meta(TimeStampedModel.Meta):
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.code})"

    def get_section_codes(self):
        """Return list of section codes from section_definitions."""
        if self.section_definitions:
            return list(self.section_definitions.keys())
        return []


class ModularLandingPage(TimeStampedModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    page_type = models.ForeignKey(
        PageType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Type of page (defines sections and item slots)",
    )
    campaign = models.ForeignKey(
        "campaigns.Campaign", on_delete=models.SET_NULL, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("modular_landing", kwargs={"slug": self.slug})

    def get_section_codes(self):
        """Get section codes from page_type."""
        if self.page_type:
            return self.page_type.get_section_codes()
        return []


# New models to support reusable items placed into page sections
class Item(TimeStampedModel):
    ITEM_TYPES = [
        ("text", "Text"),
        ("image", "Image"),
        ("video", "Video"),
        ("cta", "CTA"),
        ("link", "Link"),
        ("html", "Raw HTML"),
        ("json", "JSON Data"),
    ]

    slug = models.SlugField(
        max_length=150,
        unique=True,
        null=True,
        blank=True,
        help_text="Unique slug for stable reuse across sections/pages",
    )
    name = models.CharField(max_length=150, help_text="Internal name for editors")
    item_type = models.CharField(max_length=20, choices=ITEM_TYPES)
    text = models.TextField(blank=True)
    json = models.JSONField(
        blank=True,
        null=True,
        help_text="Structured content (title, subtitle, cta, etc.)",
    )
    image = models.ImageField(upload_to="items/", blank=True, null=True)
    file = models.FileField(upload_to="items/", blank=True, null=True)
    url = models.URLField(blank=True)
    reusable = models.BooleanField(
        default=True,
        help_text="Whether this item can be reused in multiple sections",
    )
    metadata = models.JSONField(
        blank=True,
        null=True,
        help_text="Additional extensible data for the item",
    )
    is_active = models.BooleanField(default=True)

    class Meta(TimeStampedModel.Meta):
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.item_type})"


class PageItem(TimeStampedModel):
    """Placement of an Item inside a page section."""

    page = models.ForeignKey(
        ModularLandingPage,
        on_delete=models.CASCADE,
        related_name="page_items",
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name="placements",
    )
    section_code = models.CharField(
        max_length=50, help_text="Section code (hero, benefits, cta)"
    )
    order = models.PositiveIntegerField(default=0)
    override_text = models.TextField(blank=True)
    override_json = models.JSONField(blank=True, null=True)

    class Meta(TimeStampedModel.Meta):
        ordering = ["section_code", "order"]

    def __str__(self):
        return f"{self.page.name} - {self.section_code} - {self.item.name} (Order: {self.order})"
