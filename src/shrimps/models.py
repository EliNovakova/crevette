from django.db import models
from datetime import datetime

color_choices = [
    ("pink", "pink"),
    ("white", "white"),
    ("green", "green"),
    ("red", "red"),
    ("purple", "purple"),
    ("rainbow", "rainbow"),
]


class Shrimp(models.Model):
    name = models.CharField(max_length=126)
    birth_date = models.DateTimeField(default=datetime.now())
    size = models.IntegerField()
    weight = models.IntegerField()
    color = models.CharField(max_length=32, choices=color_choices)
    is_farmed = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} the shrimp"