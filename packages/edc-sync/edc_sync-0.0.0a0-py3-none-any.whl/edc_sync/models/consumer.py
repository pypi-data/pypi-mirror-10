from django.db import models

from edc_base.model.models import BaseUuidModel


class Consumer(BaseUuidModel):

    name = models.CharField(
        max_length=25,
    )

    ipaddress = models.CharField(
        max_length=64,
    )

    is_active = models.BooleanField(
        default=True
    )

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'edc_sync'
        ordering = ['name']
