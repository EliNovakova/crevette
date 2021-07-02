
from random import randint, choice

from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse
from shrimps.forms import ShrimpForm
from shrimps.models import Shrimp


# Create your views here.


def home(request):
    """home page: display the number of shrimps inside our aquarium"""

    # num_shrimps = len(Shrimp.objects.all())
    num_shrimps = Shrimp.objects.count()
    # Shrimp.objects.all() = SELECT * FROM shrimp
    # Shrimp.objects.all() = SELECT COUNT(*) FROM shrimp

    # calling count() is more efficient than calling len() because
    # count() calls SQL-specific function COUNT which is optimized and returns only a number
    # whereas for len() we need to get all objects from the database and only then do the count locally

    # last_shrimp = Shrimp.objects.order_by('birth_date').last()
    # if last_shrimp is None:
    #     return HttpResponse(f"""There are 0 shrimps in our aquarium. """)
    # else:
    #     return HttpResponse(f"""There are {num_shrimps} shrimps in our aquarium. Last shrimp born is {last_shrimp}""")

    context = {
        "num_total_shrimps": num_shrimps,
        "shrimp_list": Shrimp.objects.all(),
    }
    return render(request, "home.html", context=context)


def give_birth_to_shrimp(request):
    """random shrimp generator: every time the page is loaded generates a new random shrimp"""

    SHRIMP_NAME_LIST = ["Richard", "Gerard", "Niky", "Hubert", "Crevette", "Paul", "Eli", "Evi"]
    # at first generate the random fields, then create a Shrimp model and populate it
    baby_shrimp_weight = randint(10, 400)
    baby_shrimp_size = randint(10, 100)
    baby_shrimp_name = choice(SHRIMP_NAME_LIST)
    baby_shrimp_color = choice(Shrimp.SHRIMP_COLOR_CHOICES)[0]  # takes first element of the returned tuple
    baby_shrimp_is_farmed = bool(randint(0, 1))
    baby_shrimp = Shrimp(name=baby_shrimp_name, size_mm=baby_shrimp_size,
                         weight_g=baby_shrimp_weight, color=baby_shrimp_color, is_farmed=baby_shrimp_is_farmed)
    baby_shrimp.save()

    context = {
        "shrimp": baby_shrimp,
    }

    return render(request, "detail.html", context=context)
    # return HttpResponse(f"""The baby shrimp {baby_shrimp.name} is born, weighs {baby_shrimp.weight_g} g and measures {baby_shrimp.size_mm} mm""")


def shrimp_detail(request, shrimp_id):
    """display detail of a particular shrimp"""

    context = {
        "shrimp": Shrimp.objects.filter(id=shrimp_id).first()
    }

    return render(request, "detail.html", context=context)


def edit_shrimp(request, shrimp_id=None):
    """edit details of a particular shrimp"""

    shrimp = Shrimp.filter(id=shrimp_id).first() if shrimp_id else None
    if request.method == "POST":
        form = ShrimpForm(data=request.POST, instance=shrimp)
        if form.is_valid():
            shrimp = form.save()
            return redirect("shrimps:detail", shrimp_id=shrimp.id)
    else:  # in this case it's a create function
        form = ShrimpForm(instance=shrimp)

    return render(request, "edit.html", context={"form": form})
