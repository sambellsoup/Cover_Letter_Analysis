from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text[:50]

class Document(models.Model):
    """Document uploaded by user to be analyzed"""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    created_at = models.DateTimeField(default=date.today)
    title = models.CharField(max_length=100)
    document = models.FileField(null=True)

    def __str__(self):
        return self.title
