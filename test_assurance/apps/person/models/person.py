from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.

class Insured(models.Model):
    first_name = models.CharField('First name', max_length=100)
    last_name = models.CharField("Last name", max_length=100)
    phone_number = models.CharField("Phone number", max_length=11)
    date_birth = models.DateField("Date of birth")
    insurance_number = models.CharField("Insurance number", max_length=12, validators=[MinLengthValidator(12)])
    national_number = models.CharField("National_number", max_length=10, validators=[MinLengthValidator(10)])

    def __str__(self):
        return self.first_name + " " + self.last_name


class Lost(models.Model):
    first_name = models.CharField('First name', max_length=100)
    last_name = models.CharField("Last name", max_length=100)
    phone_number = models.CharField("Phone number", max_length=11)
    date_birth = models.DateField("Date of birth")
    national_number = models.CharField("National_number", max_length=10, validators=[MinLengthValidator(10)])

    def __str__(self):
        return self.first_name + " " + self.last_name
