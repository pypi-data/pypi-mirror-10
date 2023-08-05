from datetime import datetime

from django.db import models

from ..edc.base.models import BaseModel

from ..fields import EncryptedTextField, FirstnameField, IdentityField
from ..mixins import CryptoMixin


class TestModel (CryptoMixin, BaseModel):

    first_name = FirstnameField(
        verbose_name="First Name")

    identity = IdentityField(
        verbose_name="Identity",
        unique=True)

    comment = EncryptedTextField(
        verbose_name="AES",
        max_length=500)

    report_date = models.DateField(
        default=datetime.today())

    objects = models.Manager()

    class Meta:
        app_label = 'django_crypto_fields'
