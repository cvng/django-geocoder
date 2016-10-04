from unittest import TestCase

from test_app.models import Place


class GeoMixinTestCase(TestCase):
    def setUp(self):
        self.place = Place()

    def test_need_geocoding_if_no_components(self):
        self.place.address = "14 Rue de Rivoli, 75004 Paris, France"

        self.assertTrue(self.place.need_geocoding())

    def test_not_need_geocoding_if_all_components(self):
        self.place.address = "14 Rue de Rivoli, 75004 Paris, France"
        self.place.locality = 'Paris'
        self.place.postal_code = '75004'
        self.place.administrative_area_level_2 = 'Paris'
        self.place.administrative_area_level_1 = 'Île-de-France'
        self.place.country = 'France'
        self.place.lat = 48.8559405
        self.place.lng = 2.3575433

        self.assertFalse(self.place.need_geocoding())

    def test_consolidate_geocoding(self):
        self.place.address = "14 Rue de Rivoli, 75004 Paris, France"
        self.place.consolidate_geocoding()

        self.assertEqual(self.place.address, "14 Rue de Rivoli, 75004 Paris, France")
        self.assertEqual(self.place.locality, 'Paris')
        self.assertEqual(self.place.postal_code, '75004')
        self.assertEqual(self.place.administrative_area_level_2, 'Paris')
        self.assertEqual(self.place.administrative_area_level_1, 'Île-de-France')
        self.assertEqual(self.place.country, 'France')

    def test_geocode_with_new_administrative_name(self):
        self.place.address = "108, Rue Leyteire, Saint-Michel - Nansouty - Saint-Genès, 33800, France"
        self.place.administrative_area_level_1 = 'Aquitaine'
        self.place.consolidate_geocoding(force=True)
        self.assertEqual(self.place.administrative_area_level_1, 'Aquitaine-Limousin-Poitou-Charentes')

    def test_geocode_with_no_results(self):
        self.place.address = "not_found"
        self.place.consolidate_geocoding(force=True)
        self.assertEqual(self.place.address, 'not_found')

    def test_geocode_without_postal_code(self):
        self.place.address = "FRANCE"
        self.place.consolidate_geocoding(commit=True, force=True)
        self.assertEqual(self.place.postal_code, None)
