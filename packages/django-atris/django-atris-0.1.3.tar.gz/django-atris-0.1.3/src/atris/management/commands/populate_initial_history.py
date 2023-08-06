from optparse import make_option

from django.core.management import BaseCommand

from atris import models
from atris.models import HistoricalRecord


class Command(BaseCommand):
    EXISTING_HISTORY_FOUND = "Existing history found, skipping model"
    option_list = BaseCommand.option_list + (
        make_option(
            '--auto',
            action='store_true',
            dest='auto',
            default=False,
            help="Automatically search for models with the "
                 "HistoricalRecords field type",
        ),
    )

    # TODO: Add option to set the additional data
    #  from the command line interface
    def handle(self, *args, **options):
        for (model, model_specific_info) in models.registered_models.items():
            additional_data_field = model_specific_info['additional_data']
            excluded_fields = model_specific_info['excluded_fields']
            self.bulk_history_create(model, additional_data_field,
                                     excluded_fields)

    def bulk_history_create(self, model, additional_data_field={},
                            excluded_fields=[]):
        """Save a copy of all instances to the historical model."""
        if HistoricalRecord.objects.filter(
                content_type__app_label=model._meta.app_label,
                content_type__model=model._meta.model_name
        ).exists():
            self.stderr.write("{msg} {model}\n".format(
                msg=self.EXISTING_HISTORY_FOUND,
                model=model,
            ))
            return

        historical_instances = [
            HistoricalRecord(
                history_user=None,
                history_type='+',
                content_object=instance,
                data=dict((unicode(field.attname),
                           unicode(getattr(instance, field.attname)))
                          for field in instance._meta.fields
                          if field.attname not in excluded_fields),
                additional_data=dict(
                    (unicode(key), unicode(value)) for (key, value)
                    in additional_data_field.items()
                )
            ) for instance in model.objects.all()]
        HistoricalRecord.objects.bulk_create(historical_instances)
