from django.test import TestCase
from django.urls import reverse
from pages.models import PageType, ModularLandingPage, Item, PageItem


class PageTypeTestCase(TestCase):
    def test_get_section_codes(self):
        pt = PageType.objects.create(
            name="Test Landing",
            code="test",
            section_definitions={
                "hero": {"items": ["text1"]},
                "benefits": {"items": ["item1"]},
            },
        )
        self.assertEqual(pt.get_section_codes(), ["hero", "benefits"])


class ModularLandingPageTestCase(TestCase):
    def setUp(self):
        self.pt = PageType.objects.create(
            name="Landing Page",
            code="landing",
            section_definitions={"hero": {"items": ["text1"]}},
        )

    def test_get_section_codes_from_page_type(self):
        page = ModularLandingPage.objects.create(
            name="Test Page", slug="test-page", page_type=self.pt
        )
        self.assertEqual(page.get_section_codes(), ["hero"])

    def test_get_section_codes_no_page_type(self):
        page = ModularLandingPage.objects.create(name="Test Page", slug="test-page")
        self.assertEqual(page.get_section_codes(), [])


class ItemTestCase(TestCase):
    def test_item_creation(self):
        item = Item.objects.create(
            name="Test Item", item_type="text", text="Hello World"
        )
        self.assertEqual(str(item), "Test Item (text)")


class PageItemTestCase(TestCase):
    def setUp(self):
        self.page = ModularLandingPage.objects.create(
            name="Test Page", slug="test-page"
        )
        self.item = Item.objects.create(
            name="Test Item", item_type="text", text="Hello"
        )

    def test_page_item_creation(self):
        pi = PageItem.objects.create(
            page=self.page, item=self.item, section_code="hero", order=0
        )
        self.assertEqual(str(pi), "Test Page - hero - Test Item (Order: 0)")


class DataSetupTestCase(TestCase):
    """Test case for setting up initial data."""

    def test_create_landing_page_type_and_webinar_page(self):
        """Test creating the landing PageType and webinar page."""
        # Create PageType 'landing'
        pt = PageType.objects.create(
            name="Landing Page",
            code="landing",
            section_definitions={
                "hero_t1": {"items": ["title", "subtitle"]},
                "benefits": {"items": ["benefit1", "benefit2", "benefit3"]},
                "cta": {"items": ["button"]},
            },
        )
        self.assertEqual(pt.code, "landing")
        self.assertIn("hero_t1", pt.get_section_codes())

        # Create webinar page
        page = ModularLandingPage.objects.create(
            name="Webinar Landing", slug="webinar", page_type=pt, is_active=True
        )
        self.assertEqual(page.slug, "webinar")
        self.assertEqual(page.page_type, pt)
        self.assertEqual(page.get_section_codes(), ["hero_t1", "benefits", "cta"])


if __name__ == "__main__":
    import pytest

    pytest.main()
