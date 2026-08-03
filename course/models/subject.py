from django.db import models
from django_extensions.db.models import TimeStampedModel
from .teacher import Teacher

class Subject(TimeStampedModel):
    title = models.CharField(max_length=100)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.title
    class Meta:
        unique_together = (('teacher',), ('title',))
