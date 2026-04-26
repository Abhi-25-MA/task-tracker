from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')

    def __str__(self):
        return self.title