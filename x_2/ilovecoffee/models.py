from django.db import models

class Coffee(models.Model):
    name = models.CharField(max_length=50)
    bean_from = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
