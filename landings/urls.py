from django.urls import path
from . import views

app_name = "landings"

urlpatterns = [
    path("", views.home, name="home"),
    path("webinar/", views.webinar_landing, name="webinar_landing"),
    path(
        "webinar/register/", views.register_webinar_lead, name="register_webinar_lead"
    ),
    path("webinar/thank-you/", views.webinar_thank_you, name="webinar_thank_you"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path("privacy-policy-technical/", views.privacy_policy_technical, name="privacy_policy_technical"),
]
