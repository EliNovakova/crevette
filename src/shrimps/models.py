from django.db import models
from django.utils import timezone


class Shrimp(models.Model):
    """ A small free-swimming crustacean with an elongated body,
    typically marine and frequently of commercial importance as food.
    """

    shrimp_colors = [
        ('PINK', 'pink'),
        ('WHITE', 'white'),
        ('GREEN', 'green'),
        ('RED', 'red'),
        ('PURPLE', 'purple'),
        ('RAINBOW', 'rainbow')
    ]

    name = models.CharField(max_length=126)
    birth_date = models.DateTimeField(default=timezone.now)
    size = models.IntegerField("size (mm)")
    weight = models.IntegerField("weight (g)")
    color = models.CharField(max_length=32, choices=shrimp_colors)
    is_farmed = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} the shrimp".capitalize()
