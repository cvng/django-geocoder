from django.apps import apps
from django.conf import settings
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Updates model address components from up-to-date Google Maps data"

    def handle(self, *args, **options):
        model = apps.get_model(settings.GEOCODER_MODEL)
        qs = model.objects.all()
        options = dict(force=True, commit=True)  # TODO: Pass options via CLI args

        self.stdout.write("Loaded %s" % model)
        for i, obj in enumerate(qs):
            obj.geocode(**options)
            self.stdout.write(
                "%s/%s, pk=%s, %s=%s" % (i + 1, qs.count(), obj.pk, model.geocoded_by, getattr(obj, model.geocoded_by)))
