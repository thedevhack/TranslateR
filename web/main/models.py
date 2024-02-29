from django.db import models


class UserIPList(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    