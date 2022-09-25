from django.db import models
from django.utils.timezone import timezone
import datetime


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
