from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name} || должность{self.position} || {self.email} || {self.phone}'

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    stage = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} || {self.email} || {self.phone}'


class SalesPipelineStage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    client = models.ManyToManyField(Client, related_name='pipeline_stages')

    def __str__(self):
        return f'{self.name} {self.client} {self.description}'




