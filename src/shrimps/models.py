from django.db import models

# Create your models here.


class Shrimp(models.Model):
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
    birth_date = models.DateTimeField('is born')
    size = models.IntegerField()
    weight = models.IntegerField()
    color = models.CharField(max_length=2, choices=SHRIMP_COLOR_CHOICES)
    is_farmed = models.BooleanField(default=True)

    # a print method
    def __str__(self):
        return f'''The shrimp {self.name} is born on {self.birth_date}, measures {self.size} mm, weights {self.weight} grams, is of color {self.get_color_display()} and is {'FARMED' if self.is_farmed else 'FREE'}'''
