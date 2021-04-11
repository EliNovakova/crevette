from django.db import models
from django.utils import timezone


class Shrimp(models.Model):
    COLOR_CHOICES = [
        ("pink", "pink"),
        ("white", "white"),
        ("green", "green"),
        ("red", "red"),
        ("purple", "purple"),
        ("rainbow", "rainbow"),
    ]
    name = models.CharField(max_length=126)
    birth_date = models.DateTimeField(default=timezone.now)
    size = models.IntegerField("mm")
    weight = models.IntegerField("g")
    color = models.CharField(max_length=32, choices=COLOR_CHOICES)
    is_farmed = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} the shrimp"
