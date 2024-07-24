from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Service(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=256, null=False, blank=False),
        description = models.TextField(null=True, blank=True)
    )
    price = models.DecimalField(max_digits=7, decimal_places=2,
                                null=True, blank=True)
    price_min = models.DecimalField(max_digits=7, decimal_places=2,
                                    null=True, blank=True)
    price_max = models.DecimalField(max_digits=7, decimal_places=2,
                                    null=True, blank=True)
