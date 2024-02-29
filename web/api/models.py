from django.db import models
from uuid import uuid4
from django.contrib.auth import get_user_model

User_Model = get_user_model()


class APIMembership(models.Model):

    identifier = models.UUIDField(primary_key=True, editable=False, default=uuid4())
    owner = models.ForeignKey(User_Model, on_delete=models.CASCADE, null=False, blank=False)
    date_registered = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    tokens = models.IntegerField(default=10)
    expiry = models.DateTimeField(null=True, blank=True)
