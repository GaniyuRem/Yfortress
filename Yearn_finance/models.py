from django.db import models

# Create your models here.
# class Contact(models.Model):


class Contact(models.Model):
    f_name = models.CharField(max_length=225)
    l_name = models.CharField(max_length=225)
    message = models.TextField(max_length=500)
