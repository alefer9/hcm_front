# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    rut = models.IntegerField(unique=True, null=True)
    direccion = models.CharField(max_length=45, null=True)
    tlf_movil = models.CharField(max_length=45, null=True, blank=True)    
    class Meta:
        db_table = 'auth_user'