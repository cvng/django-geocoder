from unittest import mock

from django.test import TestCase
from test_app.models import Place


class RegistrationTestCase(TestCase):
    def setUp(self):
        self.place = Place()

    @mock.patch('django_geocoder.mixins.GeoMixin.geocode')
    def test_geocode_on_save(self, fn):
        self.place.address = "14 Rue de Rivoli, 75004 Paris, France"
        self.place.save()
        fn.assert_called_once_with()
