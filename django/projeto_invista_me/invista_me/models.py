from django.db import models
from datetime import datetime

class Investimento(models.Model):
    investimento = models.TextField(max_length=255)
    valor = models.FloatField()
    pago = models.BooleanField()
    data = models.DateField(default=datetime.now)


# Create your models here.
