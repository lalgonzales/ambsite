# analytics/models.py
from django.db import models
from core.models import TimeStampedModel

class PageView(TimeStampedModel):
    page = models.ForeignKey('pages.Page', on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    referrer = models.URLField(blank=True)
    session_id = models.CharField(max_length=100)

    def __str__(self):
        return f"View: {self.page.title} - {self.created_at}"

class ClickEvent(TimeStampedModel):
    page = models.ForeignKey('pages.Page', on_delete=models.CASCADE)
    element_id = models.CharField(max_length=100)
    element_type = models.CharField(max_length=50)
    lead = models.ForeignKey('leads.Lead', on_delete=models.SET_NULL, null=True, blank=True)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        # safely obtain the page id: prefer the implicit page_id attribute if present,
        # otherwise fall back to the related Page object's pk (if loaded)
        page_id = getattr(self, 'page_id', None)
        if page_id is None:
            page_obj = getattr(self, 'page', None)
            page_id = getattr(page_obj, 'pk', None) if page_obj else None
        return f"Click: {self.element_id} on page_id {page_id}"
