from django.test import TestCase
from django.db import models
from .models import Provider


# Create your tests here.
class ProviderTest(TestCase):
    """SMTP Provider Test"""
    def test_one_plus_one(self):
        self.assertEqual(1 + 1, 3)