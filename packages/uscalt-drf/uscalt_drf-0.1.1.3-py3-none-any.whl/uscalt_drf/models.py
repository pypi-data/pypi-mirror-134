from django.db import models

class AuxSilo(models.Model):
    name = models.CharField(max_length=100, default=None, blank=True)
    data = models.TextField(default=None, blank=True)
    link = models.CharField(max_length=100, default=None, blank=True, null=True)
    time = models.DateTimeField(default=None, blank=True, null=True)
    data_hash = models.TextField(default=None, blank=True, null=True)

class IntentSilo(models.Model):
    identifier = models.CharField(max_length=100, default=None, blank=True)
    link = models.CharField(max_length=100, default=None, blank=True, null=True)