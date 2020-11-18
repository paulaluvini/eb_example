from django.db import models

# Create your models here.


class Persona(models.Model):
    name = models.TextField()

class NumeroHistorico(models.Model):
    number = models.DecimalField(decimal_places=60,max_digits=100)
    created_at = models.DateTimeField(auto_now=True)
    request_information = models.TextField(blank=True)
    ip = models.TextField(blank=True)
    port = models.IntegerField(default=-1)
    persona = models.ForeignKey('Persona',on_delete=models.SET_NULL,null=True)
