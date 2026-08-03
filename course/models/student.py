from django.db import models
from django_extensions.db.models import TimeStampedModel

class Student(TimeStampedModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    time = models.TimeField()
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

