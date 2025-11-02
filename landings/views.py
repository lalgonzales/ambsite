from django.shortcuts import render, redirect
from django.contrib import messages
from analytics.models import Lead  # pragma: no cover


def home(request):
    """Home page - redirects to main webinar landing"""
    return redirect("landings:webinar_landing")


def webinar_landing(request):
    """Main webinar landing page"""
    context = {
        "page_title": "Webinar Exclusivo",
        "meta_description": "Descubre cómo transformar tu negocio en solo 60 minutos",
    }
    return render(request, "landings/webinar.html", context)


def register_webinar_lead(request):
    """Handle webinar lead registration"""
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone", "")

        # Validación básica
        if not name or not email:
            messages.error(request, "Por favor completa todos los campos requeridos.")
            return redirect("landings:webinar_landing")

        # Guardar el lead
        try:
            Lead.objects.create(name=name, email=email, phone=phone, source="webinar")

            messages.success(request, "¡Registro exitoso! Te contactaremos pronto.")
            return redirect("landings:webinar_thank_you")

        except Exception as e:
            # Manejar específicamente el error de email duplicado
            if "UNIQUE constraint failed" in str(e) or "duplicate key value" in str(e):
                messages.warning(
                    request,
                    "Este email ya está registrado. Te contactaremos pronto si aún no lo hemos hecho.",
                )
                return redirect("landings:webinar_thank_you")
            else:
                messages.error(
                    request,
                    "Hubo un error en el registro. Por favor intenta nuevamente.",
                )
                return redirect("landings:webinar_landing")

    return redirect("landings:webinar_landing")


def webinar_thank_you(request):
    """Thank you page after registration"""
    return render(request, "landings/webinar_thank_you.html")


def privacy_policy(request):
    """Simple privacy policy page"""
    context = {
        "page_title": "Política de Privacidad",
        "meta_description": "Política de privacidad simple y clara para la Master Class SIG",
    }
    return render(request, "landings/privacy_policy_simple.html", context)


def privacy_policy_technical(request):
    """Technical privacy policy page"""
    context = {
        "page_title": "Política de Privacidad (Técnica)",
        "meta_description": "Versión técnica de nuestra política de privacidad - datos recopilados y uso",
    }
    return render(request, "landings/privacy_policy_technical.html", context)
