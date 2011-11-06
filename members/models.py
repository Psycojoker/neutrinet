from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    statut = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    mail = models.EmailField()
    mail_alias = models.EmailField()
    cotisation = models.DateField()
