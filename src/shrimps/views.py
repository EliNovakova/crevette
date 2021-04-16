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

    last_shrimp = Shrimp.objects.order_by('-birth_date')[0]

    return HttpResponse(f"""There are {num_shrimps} shrimps in our aquarium. Last shrimp born is {last_shrimp}""")
