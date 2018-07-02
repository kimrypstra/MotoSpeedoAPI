from django.db import models

# Create your models here.

class Key(models.Model):
    string = models.TextField()
    date = models.DateField()
    test = models.BooleanField(default=False)
    deprecated = models.BooleanField(default=False)
