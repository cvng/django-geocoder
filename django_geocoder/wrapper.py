import geocoder as _geocoder
from django.conf import settings
from memoize import memoize

__all__ = ['geocoder']


class Geocoder(object):
    """
    Simple wrapper that adds caching support to geocoding providers.
    """

    @memoize()
    def get(self, location, **kwargs):
        default_provider = {
            'provider': 'google',
            'language': 'fr',
            'key': getattr(settings, 'GOOGLEMAPS_BACKEND_KEY', None)}

        provider = {}
        provider.update(default_provider)
        provider.update(kwargs)
        result = _geocoder.get(location, method='geocode', **provider)

        if not result.ok:
            result = _geocoder.get(location, method='geocode', **default_provider)

        return result


geocoder = Geocoder()
