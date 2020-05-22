from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Client(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients', null=True, blank=True)
    last_login_date = models.DateField(default=timezone.now, null=True, blank=True)
    points = models.IntegerField()