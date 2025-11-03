from django.shortcuts import render
from .models import Lead
from .forms import LeadForm


def capture_lead(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save()
            # Future enhancement: send a confirmation email to the lead
            return render(request, "pages/thank_you.html")
    else:
        form = LeadForm()
    return render(request, "leads/capture_lead.html", {"form": form})
