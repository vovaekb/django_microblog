from django.db import models
from django.utils import timezone


class Post(models.Model):
    '''
    Stores a single blog post
    '''
    title = models.CharField(max_length=100, null=True)
    text = models.TextField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Text: {self.text}"
