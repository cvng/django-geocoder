# django-geocoder
[![PyPI version](https://badge.fury.io/py/django-geocoder.svg)](https://badge.fury.io/py/django-geocoder)
[![Build Status](https://travis-ci.org/cvng/django-geocoder.svg?branch=master)](https://travis-ci.org/cvng/django-geocoder)

Python [geocoder][1] wrapper for Django, inspired by Ruby [geocoder][2].

## How it works

Looks for an `geocoded_by` attribute (default = `address`) in your `GEOCODER_MODEL` and fills the `required_address_components` with geocoding data.

## Install

```python
# settings.py
GEOCODER_MODEL = 'test_app.Place'
```

## Usage

### As a mixin

```python
from django.db import models
from django_geocoder.mixins import GeoMixin

class Place(models.Model, GeoMixin):
    address = models.CharField()

    # [...] locality, postal_code, etc...

    required_address_components = {
        'locality': ['locality'],
        'postal_code': ['postal_code'],
    }
```

### As a Django command

Performs a geocoding on all objects

```bash
$ python manage.py batch_geocode
```

### As an helper for caching

```python
import django_geocoder as geocoder

# calls `geocoder.get()` under the hoods
result = geocoder.get("Some address")

# same as above, with caching
result = geocoder.get_cached("Some address")
```

[1]: (https://github.com/DenisCarriere/geocoder)
[2]: (https://github.com/alexreisner/geocoder)
