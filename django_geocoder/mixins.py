import warnings

from django_geocoder.wrapper import get_cached


class GeoMixin(object):
    # Overridable by subclasses
    geocoded_by = 'address'

    def need_geocoding(self):
        """
        Returns True if any of the required address components is missing
        """
        need_geocoding = False
        for attribute, component in self.required_address_components.items():
            if not getattr(self, attribute):
                need_geocoding = True
                break  # skip extra loops
        return need_geocoding

    def geocode(self, commit=False, force=False):
        """
        Do a backend geocoding if needed
        """
        if self.need_geocoding() or force:
            result = get_cached(getattr(self, self.geocoded_by), provider='google')
            if result.status == 'OK':
                for attribute, components in self.required_address_components.items():
                    for component in components:
                        if not getattr(self, attribute) or force:
                            attr_val = getattr(result, component, None)
                            if attr_val:
                                setattr(self, attribute, attr_val)

            if commit:
                self.save()

    def consolidate_geocoding(self, *args, **kwargs):
        warnings.warn(
            "Usage of consolidate_geocoding() is deprecated. Use geocode() instead", DeprecationWarning)
        return self.geocode(*args, **kwargs)

    def save(self, *args, **kwargs):
        """
        Extends model ``save()`` to allow dynamic geocoding
        """
        self.geocode()
        return super(GeoMixin, self).save(*args, **kwargs)
