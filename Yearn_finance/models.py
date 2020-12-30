from django.db import models

# Create your models here.
# class Contact(models.Model):

from django.db import models

# Create your models here.
# class Contact(models.Model):


class Contact(models.Model):
    full_name = models.CharField(max_length=225)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=500)
