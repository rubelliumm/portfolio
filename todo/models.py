from django.db import models
from django.utils import timezone


class Todo(models.Model):
    importance_choices = (
        ('⭐', '1 star'),
        ('⭐⭐', '2 star'),
        ('⭐⭐⭐', '3 star'),
        ('⭐⭐⭐⭐', '4 star'),
        ('⭐⭐⭐⭐⭐', '5 star'),
    )
    name = models.CharField(max_length=100)
    detail = models.TextField(blank=True)
    created = models.DateTimeField(default=timezone.now)
    importance = models.CharField(
        max_length=5, choices=importance_choices, blank=True)

    def __str__(self):
        return self.name
