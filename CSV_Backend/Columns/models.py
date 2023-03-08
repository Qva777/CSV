from faker import Faker
from django.db import models
from CSV_Backend.Schemas.models import Schema

fake = Faker()


class Column(models.Model):
    """ Column Model """
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name='columns')
    full_name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    job = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    domain = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    integer = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        """ String representation """
        return self.schema.name

    class Meta:
        """ Representation in admin panel """
        verbose_name = 'Columns'
        verbose_name_plural = 'Columns'
