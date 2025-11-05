# pages/models.py
from django.db import models
from core.models import TimeStampedModel


class Page(TimeStampedModel):
    PAGE_TYPES = [
        ("landing", "Landing Page"),
        ("sales", "Sales Page"),
        ("thank_you", "Thank You Page"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    page_type = models.CharField(max_length=20, choices=PAGE_TYPES)
    is_active = models.BooleanField(default=True)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)

    def __str__(self):
        return str(self.title)

    def get_default_sections(self):
        defaults = {
            "landing": [
                {"type": "hero", "data": {}},
                {"type": "benefits", "data": {}},
                {"type": "cta", "data": {}},
                {"type": "testimonials", "data": {}},
            ],
            "sales": [
                {"type": "hero", "data": {}},
                {"type": "benefits", "data": {}},
                {"type": "cta", "data": {}},
            ],
            "thank_you": [
                {"type": "hero", "data": {}},
            ],
        }
        key = getattr(self, "page_type", "")
        return defaults.get(str(key), [])


class Section(TimeStampedModel):
    SECTION_TYPES = [
        ("hero", "Hero Section"),
        ("benefits", "Benefits Section"),
        ("cta", "Call to Action Section"),
        ("testimonials", "Testimonials Section"),
    ]
    page = models.ForeignKey(Page, related_name="sections", on_delete=models.CASCADE)
    section_type = models.CharField(max_length=50, choices=SECTION_TYPES)
    order = models.PositiveIntegerField(default=0)
    data = models.JSONField(
        default=dict,
        blank=True,
        help_text="Specific data for the section in JSON format",
    )

    class Meta(TimeStampedModel.Meta):
        ordering = ["order"]

    def __str__(self):
        return f"{self.section_type} for {self.page.title}"
