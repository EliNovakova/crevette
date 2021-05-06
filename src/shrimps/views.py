from django.shortcuts import render
from django.http import HttpResponse
from shrimps.models import Shrimp
from random import randint, choice


def home(request):
    """Home page: display the number of shrimp in our aquarium."""

    num_shrimps = Shrimp.objects.count()
    all_shrimps = Shrimp.objects.all()
    # num_shrimps = len(Shrimp.objects.all())

    # count() - returns an int representing the number of objects in database
    # is better option if all we want to do it to get the count and not iterate over the results as len() does

    # SELECT * FROM shrimp  (what len() does)
    # SELECT COUNT(*) FROM shrimp (what count() does)

    content1 = f"""There are {num_shrimps} shrimps in our aquarium."""

    last_shrimp_born = Shrimp.objects.order_by('birth_date').last()   # orders by birth date asc, displays the last
    if last_shrimp_born is not None:    # if there are shrimp in our aquarium
        content1 += f"""The last shrimp born is {last_shrimp_born}."""  # adds this to the content

    context = {
        "num_total_shrimps": num_shrimps,
        "all_shrimps": all_shrimps
    }
    return render(request, template_name="home.html", context=context)


def give_birth_to_shrimp(request):
    """Creates a new shrimp with random name, size, weight and color and saves it to the database
    every time the page reloads."""
    names = ["Max", "Cooper", "Ollie", "Walter", "Apollo", "Milo", "Billy", "Gerard"]
    name = choice(names)
    size = randint(10, 40)
    weight = randint(1, 10)
    color = choice(Shrimp.COLOR_CHOICES)[0]     # returns tuple, [0] takes its first item
    is_farmed = bool(randint(0, 1))

    new_shrimp = Shrimp(name=name, size=size, weight=weight, color=color, is_farmed=is_farmed)
    new_shrimp.save()

    context = {
        "shrimp": new_shrimp,
    }
    return render(request, template_name="detail.html", context=context)


def shrimp_detail(request, shrimp_id):
    """Display detail of shrimp."""
    shrimp = Shrimp.objects.get(id=shrimp_id)

    context = {
        "shrimp": shrimp,
    }
    return render(request, template_name="detail.html", context=context)


