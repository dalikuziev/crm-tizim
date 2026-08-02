from django.db import models
from django_extensions.db.models import TimeStampedModel

class Subject(TimeStampedModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title
