from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, editable=True, blank=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
