from django.shortcuts import render


def home(request):
    context = {"title": "Inicio - Mi Sitio Web", "page_name": "Página Principal"}
    return render(request, "landings/home.html", context)


def servicios(request):
    return render(request, "landings/servicios.html", {"title": "Servicios"})


def contacto(request):
    return render(request, "landings/contacto.html", {"title": "Contacto"})
