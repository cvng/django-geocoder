from django.db import models

from django_geocoder.mixins import GeoMixin


class Place(GeoMixin, models.Model):
    address = models.CharField(max_length=255, blank=True, null=True)
    locality = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    administrative_area_level_1 = models.CharField(max_length=255, blank=True, null=True)
    administrative_area_level_2 = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    # The list of attributes to update after geocoding
    required_address_components = {
        'address': ['address'],
        'locality': ['city', 'town', 'locality'],
        'postal_code': ['postal'],
        'administrative_area_level_2': ['county'],
        'administrative_area_level_1': ['state'],
        'country': ['country_long'],
        'lat': ['lat'],
        'lng': ['lng'],
    }
