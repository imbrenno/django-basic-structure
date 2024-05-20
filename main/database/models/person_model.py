from django.db import models
from main.helpers.enums.gender import GenderEnum


class Person(models.Model):
    name = models.CharField(max_length=30)
    date_birth = models.DateField()
    document = models.CharField()
    gender = models.CharField(
        max_length=1,
        choices=GenderEnum.choices(),
        default=GenderEnum.OTHER.value,
    )
    height = models.FloatField()
    weight = models.FloatField()

    # def to_json(self):
    #     return {
    #         "name": self.name,
    #         "date_birth": self.date_birth,
    #         "document": self.document,
    #         "gender": self.get_gender_display(),
    #         "height": self.height,
    #         "weight": self.weight,
    #     }
