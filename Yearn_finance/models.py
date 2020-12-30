from django.db import models

# Create your models here.
# class Contact(models.Model):

<<<<<<< HEAD
from django.db import models

# Create your models here.
# class Contact(models.Model):


class Contact(models.Model):
    full_name = models.CharField(max_length=225)
    email = models.EmailField(max_length=254)
=======

class Contact(models.Model):
    f_name = models.CharField(max_length=225)
    l_name = models.CharField(max_length=225)
>>>>>>> b828d8e30ae34c335fc9150203a66c373a50b557
    message = models.TextField(max_length=500)
