from django.shortcuts import render
from django.http import HttpResponse
from shrimps.models import Shrimp
from random import randint, choice


def home(request):
    """Home page: display the number of shrimp in our aquarium."""

    num_shrimps = Shrimp.objects.count()
    # num_shrimps = len(Shrimp.objects.all())

    # count() - returns an int representing the number of objects in database
    # is better option if all we want to do it to get the count and not iterate over the results as len() does

    # SELECT * FROM shrimp  (what len() does)
    # SELECT COUNT(*) FROM shrimp (what count() does)

    last_shrimp_born = Shrimp.objects.order_by('-birth_date').first()   # orders by birth date desc, displays the first
    return HttpResponse(f"""There are {num_shrimps} shrimps in our aquarium. The last shrimp born is 
                        {last_shrimp_born}.""")


def give_birth_to_shrimp(request):
    """Creates a new shrimp with random name, size, weight and color and saves it to the database
    every time the page reloads."""
    names = ["Max", "Cooper", "Ollie", "Walter", "Apollo", "Milo", "Billy"]
    name= choice(names)
    size = randint(10, 40)
    weight = randint(1, 10)
    color = choice(Shrimp.COLOR_CHOICES)

    new_shrimp = Shrimp(name=name, size=size, weight=weight, color=color)
    new_shrimp.save()
    # difference between save() and objects.create()?

    return HttpResponse(
         f"""A new baby shrimp named {name} is born, it weights {weight} g and measures {size} mm.""")






