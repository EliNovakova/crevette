
from random import randint, choice

from django.shortcuts import render

from django.http import HttpResponse
from shrimps.models import Shrimp


# Create your views here.


def home(request):
    """home page: display the number of shrimps inside our aquarium"""

    # num_shrimps = len(Shrimp.objects.all())
    num_shrimps = Shrimp.objects.count()
    # Shrimp.objects.all() = FROM shrimp SELECT *
    # Shrimp.objects.all() = FROM shrimp SELECT COUNT(*)

    # calling count() is more efficient than calling len() because
    # count() calls SQL-specific function COUNT which is optimized and returns only a number
    # whereas for len() we need to get all objects from the database and only then do the count locally

    last_shrimp = Shrimp.objects.order_by('birth_date').last()
    if last_shrimp is None:
        return HttpResponse(f"""There are 0 shrimps in our aquarium. """)
    else:
        return HttpResponse(f"""There are {num_shrimps} shrimps in our aquarium. Last shrimp born is {last_shrimp}""")


def give_birth_to_shrimp(request):
    """random shrimp generator: every time the page is loaded generates a new random shrimp"""

    SHRIMP_NAME_LIST = ["Richard", "Gerard", "Niky", "Hubert", "Crevette", "Paul", "Eli", "Evi"]
    # at first generate the random fields, then create a Shrimp model and populate it
    baby_shrimp_weight = randint(10, 400)
    baby_shrimp_size = randint(10, 100)
    baby_shrimp_name = choice(SHRIMP_NAME_LIST)
    baby_shrimp_color = choice(Shrimp.SHRIMP_COLOR_CHOICES)[0]  # takes first element of the returned tuple
    baby_shrimp = Shrimp(name=baby_shrimp_name, size_mm=baby_shrimp_size,
                         weight_g=baby_shrimp_weight, color=baby_shrimp_color)
    baby_shrimp.save()
    return HttpResponse(f"""The baby shrimp {baby_shrimp.name} is born, weighs {baby_shrimp.weight_g} g and measures {baby_shrimp.size_mm} mm""")
