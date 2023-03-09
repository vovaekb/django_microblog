from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Text: {self.text}"
