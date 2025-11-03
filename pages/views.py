from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page
from .models import ModularLandingPage
from leads.forms import LeadForm
import json


@cache_page(60 * 15)  # 15-minute cache
def modular_landing_page(request, slug):
    landing_page = get_object_or_404(ModularLandingPage, slug=slug, is_active=True)
    # Lead form (can be in multiple sections)
    lead_form = LeadForm()

    # Build a dict of sections -> list of entries so templates can render
    # without complex logic. Each entry contains the item object, resolved data
    # and html.
    section_data = {}
    for section_code in landing_page.get_section_codes():
        items_qs = getattr(landing_page, "page_items", None)
        if items_qs and items_qs.filter(section_code=section_code).exists():
            for pi in (
                items_qs.filter(section_code=section_code)
                .select_related("item")
                .order_by("order")
            ):
                item = pi.item
                # resolve data/html from overrides or item
                data = pi.override_json or getattr(item, "json", None)
                html = pi.override_text or (
                    item.text
                    if getattr(item, "item_type", None) in ("html", "text")
                    else None
                )
                entry = {"item": item, "data": data, "html": html}
                section_data.setdefault(section_code, []).append(entry)
        else:
            # Fallback: empty list or default content if needed
            section_data.setdefault(section_code, [])

    if request.method == "POST" and "capture_lead" in request.POST:
        lead_form = LeadForm(request.POST)
        if lead_form.is_valid():
            lead = lead_form.save(commit=False)
            if landing_page.campaign:
                lead.campaign = landing_page.campaign
            lead.save()
            # Redirect to thank you page or show message
            return render(
                request, "pages/thank_you.html", {"landing_page": landing_page}
            )

    context = {
        "landing_page": landing_page,
        "lead_form": lead_form,
        "section_data": section_data,
    }

    return render(request, "pages/modular_landing.html", context)


def home(request):
    """Redirect root of pages/ to the webinar landing (or first active landing).

    This avoids infinite redirects by redirecting to the slug-based view
    (which renders the landing) instead of to another redirecting URL.
    """
    # prefer explicit 'webinar' slug
    landing = ModularLandingPage.objects.filter(slug="webinar", is_active=True).first()
    if not landing:
        landing = ModularLandingPage.objects.filter(is_active=True).first()

    if landing:
        return redirect("pages:modular_landing", slug=landing.slug)

    # fallback: simple response if no landing configured
    from django.http import HttpResponse

    return HttpResponse("No landing configured", status=404)
