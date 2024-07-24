from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from phonenumber_field.modelfields import PhoneNumberField


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

    def price_field(self):
        if self.price_min and self.price_max:
            return f'₪{self.price.min} - ₪{self.price.max}'
        elif self.price_min and not self.price_max:
            return f'from ₪{self.price.min}'
        elif not self.price_min and self.price_max:
            return f'up to ₪{self.price.max}'
        else:
            return f'₪{self.price}'


class Bid(TranslatableModel):
    translations = TranslatedFields(
        text = models.TextField(null=False, blank=False)
    )
    email = models.EmailField(null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    
