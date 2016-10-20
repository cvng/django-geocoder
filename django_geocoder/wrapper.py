import geocoder
from django.core.cache import cache


def get_cached(location, **kwargs):
    """
    Simple wrapper that adds Django caching support to 'geocoder.get()'.
    """
    result = cache.get(location)

    # Result is not cached or wrong
    if not result or not result.ok:
        result = geocoder.get(location, **kwargs)
        if result.ok:
            cache.set(location, result)

    return result
