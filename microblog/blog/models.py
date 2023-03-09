from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    text = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, default=timezone.now)

    def __str__(self):
        return f"Text: {self.text}"
