from django.db import models
from main.helpers.enums.gender import GenderEnum


class Person(models.Model):
    name = models.CharField(max_length=30)
    date_birth = models.DateField()
    document = models.BigIntegerField()
    gender = models.CharField(
        max_length=1,
        choices=GenderEnum.choices(),
        default=GenderEnum.OTHER.value,
    )
    height = models.FloatField()
    weight = models.FloatField()
