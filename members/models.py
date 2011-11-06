from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    statut = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    email_alias = models.EmailField(null=True, blank=True)
    cotisation = models.DateField(null=True, blank=True)
    adhesion = models.DateField(null=True, blank=True)
    demande = models.DateField(null=True, blank=True)
