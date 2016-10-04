from unittest import TestCase

from django.core.management import call_command
from test_app.models import Place


class BatchGeocodeTestCase(TestCase):
    def setUp(self):
        self.place = Place()

    def test_batch_geocode(self):
        self.place.address = "14 Rue de Rivoli, 75004 Paris, France"
        self.place.save()

        call_command('batch_geocode')
        self.place.refresh_from_db()

        self.assertIsNotNone(self.place.locality)
