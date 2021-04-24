from django.db import models
from django.utils import timezone

# Create your models here.


class Shrimp(models.Model):
    # constants - should be upper case letters
    PINK = 'PI'
    WHITE = 'WH'
    GREEN = 'GR'
    RED = 'RE'
    PURPLE = 'PU'
    RAINBOW = 'RA'
    SHRIMP_COLOR_CHOICES = [
        (PINK, 'Pink'),
        (WHITE, 'White'),
        (GREEN, 'Green'),
        (RED, 'Red'),
        (PURPLE, 'Purple'),
        (RAINBOW, 'Rainbow'),
    ]
    name = models.CharField(max_length=126)
    # not now() because in that case the function would be executed straight away but we want to execute it at creation of the object
    birth_date = models.DateTimeField('Birth Date', default=timezone.now)
    size_mm = models.IntegerField('Size (mm)')
    weight_g = models.IntegerField('Weight (g)')
    color = models.CharField(max_length=2, choices=SHRIMP_COLOR_CHOICES)
    is_farmed = models.BooleanField(default=True)

    # a print method
    def __str__(self):
        return f'''{self.name} the shrimp'''
