# -*- coding:Utf-8 -*-
from django.db import models

STATUT = (
    (u'ca', u'membre du CA'),
    (u'president', u'président'),
    (u'vice-president', u'vice-président'),
    (u'secretaire', u'secrétaire'),
    (u'vice-secretaire', u'vice-secrétaire'),
    (u'tresorier', u'trésorier'),
    (u'tresorier-adjoint', u'trésorier adjoint'),
    (u'membre-effectif', u'membre effectif'),
    (u'membre-adherent', u'membre adhérent'),
    (u'candidat-membre', u'candidat membre'),
)

class Member(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    statut = models.CharField(max_length=255, choices=STATUT, default="candidat-membre")
    address = models.CharField(max_length=255)
    email = models.EmailField()
    email_alias = models.EmailField(null=True, blank=True)
    cotisation = models.DateField(null=True, blank=True)
    adhesion = models.DateField(null=True, blank=True)
    demande = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return "%s %s" % (self.surname, self.name)
