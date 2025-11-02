from django.test import TestCase
from django.urls import reverse
from .models import Lead


class LeadModelTest(TestCase):
    def test_lead_creation(self):
        """Test that a lead can be created"""
        lead = Lead.objects.create(
            name="Test User", email="test@example.com", phone="123456789", source="test"
        )
        self.assertEqual(lead.name, "Test User")
        self.assertEqual(lead.email, "test@example.com")
        self.assertEqual(lead.status, "new")

    def test_lead_str_method(self):
        """Test the string representation of Lead"""
        lead = Lead.objects.create(name="Test User", email="test@example.com")
        self.assertEqual(str(lead), "Test User - test@example.com")

    def test_lead_unique_email(self):
        """Test that email must be unique"""
        Lead.objects.create(name="User 1", email="test@example.com")
        with self.assertRaises(Exception):
            Lead.objects.create(name="User 2", email="test@example.com")
