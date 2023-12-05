from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
