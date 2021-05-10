from django.db import models

# Create your models here.
from django.core.validators import MinLengthValidator
from django.db import models

from django.contrib.auth.models import User


class Account(models.Model):
    CHOICE_ROL = [('0', 'insurer'), ('1', 'Assessor expert'), ('2', 'Admin')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=1, choices=CHOICE_ROL)

    def __str__(self):
        return self.user.username

    class Meta:
        abstract = True


class Insurer(Account):
    insurer_number = models.CharField('Insurer number', max_length=10)
    established_year = models.CharField(max_length=4, validators=[MinLengthValidator(4)])
    name=models.CharField(max_length=60,null=True)


class AssessorExpert(Account):
    first_name = models.CharField('First name', max_length=100)
    last_name = models.CharField("Last name", max_length=100)
    phone_number = models.CharField("Phone number", max_length=11)
    work_experience_years = models.CharField(" Number of years of work experience", max_length=2)


class Admin(Account):
    first_name = models.CharField('First name', max_length=100)
    last_name = models.CharField("Last name", max_length=100)
    phone_number = models.CharField("Phone number", max_length=11)

    def save(self,*args, **kwargs):
        self.id_staff = True
        super().save(*args, **kwargs)

