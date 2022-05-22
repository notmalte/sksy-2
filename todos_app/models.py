from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    deadline = models.DateField()
    percent_done = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
