# core/context_processors.py
from django.conf import settings


def tracking_config(request):
    return {
        "GTM_ID": settings.GTM_ID if hasattr(settings, "GTM_ID") else "",
        "FB_PIXEL_ID": (
            settings.FB_PIXEL_ID if hasattr(settings, "FB_PIXEL_ID") else ""
        ),
        "DEBUG": settings.DEBUG,
    }
