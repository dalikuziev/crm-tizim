from django.db import models
from django_extensions.db.models import TimeStampedModel
from .student import Student

class Teacher(TimeStampedModel):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    birth_date = models.DateField()
    student = models.ManyToManyField(
        Student,
        related_name='teachers'
    )
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    class Meta:
        unique_together = (('phone_number',),)
