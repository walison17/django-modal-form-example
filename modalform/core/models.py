import json

from django.db import models
from django.core.serializers.json import DjangoJSONEncoder


class Team(models.Model):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=64)
    foundry_date = models.DateField()

    def __str__(self):
        return self.name

    def to_json(self):
        data = {
            'name': self.name,
            'country': self.country,
            'foundry_date': self.foundry_date
        }

        return json.dumps(data, cls=DjangoJSONEncoder)
