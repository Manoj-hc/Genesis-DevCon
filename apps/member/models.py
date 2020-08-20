import time
import uuid
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class DevconMember(models.Model):
    uuid = models.UUIDField('User uuid', default=uuid.uuid4)
    email = models.EmailField('Email')
    name = models.CharField("Name", max_length=128)
    phone = models.CharField("Phone", max_length=32, null=True)
    company = models.CharField("Company", max_length=256, null=True)
    designation = models.CharField("Designation", max_length=256, null=True)
    date_created = models.DateTimeField("Date created", auto_now_add=True)

    def __str__(self):
        return self.email


class Speaker(models.Model):
    # Ideally, we should have created an abstract model with common fields
    uuid = models.UUIDField('User uuid', default=uuid.uuid4)
    email = models.EmailField('Email')
    name = models.CharField("Name", max_length=128)
    phone = models.CharField("Phone", max_length=32, null=True)
    company = models.CharField("Company", max_length=256, null=True)
    designation = models.CharField("Designation", max_length=256, null=True)
    date_created = models.DateTimeField("Date created", auto_now_add=True)
    topic = models.CharField("Topic", max_length=256, null=True)
    topic_desc = models.CharField("Topic description", max_length=512, null=True)

    def __str__(self):
        return self.email


class Prospect(models.Model):
    # Ideally, we should have created an abstract model with common fields
    uuid = models.UUIDField('User uuid', default=uuid.uuid4)
    email = models.EmailField('Email')
    date_created = models.DateTimeField("Date created", auto_now_add=True)

    def __str__(self):
        return self.email
