from django.shortcuts import render, get_object_or_404
from django.conf import settings

from .models import Page


def landing_page(request, slug):
    page = get_object_or_404(Page, slug=slug, is_active=True)
    sections = page.sections.all()
    if not sections.exists():
        sections = page.get_default_sections()

    context = {
        "page": page,
        "sections": sections,
        "GTM_ID": settings.GTM_ID,
        "FB_PIXEL_ID": settings.FB_PIXEL_ID,
    }

    return render(request, "pages/landing.html", context)
