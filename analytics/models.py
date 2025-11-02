from django.db import models


class Lead(models.Model):
    # Datos básicos
    name = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    phone = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Teléfono"
    )

    # Tracking
    source = models.CharField(max_length=50, default="direct", verbose_name="Fuente")
    campaign = models.ForeignKey(
        "landings.Campaign",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Campaña",
    )
    landing_page = models.ForeignKey(
        "landings.LandingPage",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Página de Landing",
    )

    # Status y seguimiento
    STATUS_CHOICES = [
        ("new", "Nuevo"),
        ("contacted", "Contactado"),
        ("qualified", "Calificado"),
        ("converted", "Convertido"),
        ("lost", "Perdido"),
    ]
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="new", verbose_name="Estado"
    )

    # Timestamps
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Última Actualización"
    )

    # UTM parameters
    utm_source = models.CharField(max_length=100, blank=True, verbose_name="UTM Source")
    utm_medium = models.CharField(max_length=100, blank=True, verbose_name="UTM Medium")
    utm_campaign = models.CharField(
        max_length=100, blank=True, verbose_name="UTM Campaign"
    )

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = "Lead"
        verbose_name_plural = "Leads"
        ordering = ["-created_at"]
