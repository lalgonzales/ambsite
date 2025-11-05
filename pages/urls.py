from django.urls import path

from . import views

urlpatterns = [
    path("<slug:slug>/", views.landing_page, name="landing_page"),
]
