from unittest import TestCase, mock

from django.core.cache import cache
from django_geocoder.wrapper import get_cached


class GeocoderResultOk:
    ok = True


class GeocoderResultNotOk:
    ok = False


class GeocoderWrapperTestCase(TestCase):
    def setUp(self):
        # clear cache before each tests
        cache.clear()

    @mock.patch('geocoder.get', return_value=GeocoderResultOk)
    def test_result_is_cached(self, *_):
        address = 'something_to_geocode'

        get_cached(address)

        self.assertTrue(cache.get(address))

    @mock.patch('geocoder.get', return_value=GeocoderResultOk)
    def test_geocoder_not_called_for_cached_result(self, geocoder):
        address = 'something_to_geocode'

        get_cached(address)  # call geocode, set cache
        get_cached(address)  # no geocode, read cache

        geocoder.assert_called_once_with(address)

    @mock.patch('geocoder.get', return_value=GeocoderResultNotOk)
    def test_result_not_cached_if_error(self, *_):
        address = 'something_to_geocode'

        get_cached(address)

        self.assertIsNone(cache.get(address))

    @mock.patch('geocoder.get', return_value=GeocoderResultOk)
    def test_cached_result_not_returned_if_error(self, *_):
        address = 'something_to_geocode'
        cache.set(address, GeocoderResultNotOk())

        result = get_cached(address)

        self.assertTrue(result.ok)

    @mock.patch('geocoder.get', return_value=GeocoderResultOk)
    def test_result_invalidated_if_error(self, *_):
        address = 'something_to_geocode'
        cache.set(address, GeocoderResultNotOk())

        get_cached(address)

        self.assertTrue(cache.get(address).ok)
