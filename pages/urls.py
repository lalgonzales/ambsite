from django.urls import path
from django.shortcuts import redirect

from . import views

app_name = "pages"

urlpatterns = [
    # home redirects to the webinar landing (or first active landing)
    path("", views.home, name="home"),
    path("<slug:slug>/", views.modular_landing_page, name="modular_landing"),
]
