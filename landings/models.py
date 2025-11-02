from django.db import models
from django.utils.text import slugify


class Campaign(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre de la Campaña")
    description = models.TextField(blank=True, verbose_name="Descripción")
    is_active = models.BooleanField(default=True, verbose_name="Activa")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Campaña"
        verbose_name_plural = "Campañas"
        ordering = ["-created_at"]


class LandingPage(models.Model):
    campaign = models.ForeignKey(
        Campaign, on_delete=models.CASCADE, verbose_name="Campaña"
    )
    title = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    template = models.CharField(
        max_length=100, default="webinar.html", verbose_name="Template"
    )

    # Configuración
    meta_description = models.TextField(blank=True, verbose_name="Meta Description")
    cta_button_text = models.CharField(
        max_length=100, default="Registrarme", verbose_name="Texto del Botón CTA"
    )
    whatsapp_number = models.CharField(
        max_length=20, default="1234567890", verbose_name="Número de WhatsApp"
    )

    # Analytics
    view_count = models.PositiveIntegerField(default=0, verbose_name="Vistas")
    conversion_count = models.PositiveIntegerField(
        default=0, verbose_name="Conversiones"
    )

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación"
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.campaign.name})"

    class Meta:
        verbose_name = "Página de Landing"
        verbose_name_plural = "Páginas de Landing"
        ordering = ["-created_at"]
