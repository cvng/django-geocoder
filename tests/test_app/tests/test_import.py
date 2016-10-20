import django_geocoder
from django.test import TestCase


class GeocoderImportTestCase(TestCase):
    def test_base_geocoder_functions_imported(self):
        # The wrapper should exposes all 'geocoder' functions plus the new ones
        self.assertTrue(hasattr(django_geocoder, 'get'))
