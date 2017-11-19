
from django.db import models


class Blog(models.Model):
    full_name = models.CharField(max_length=25)
    age = models.IntegerField()
