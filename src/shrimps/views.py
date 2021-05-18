from random import randint, choice

from django.shortcuts import render, get_object_or_404

from shrimps.models import Shrimp


def home(request):
    """ home page: display the numbers of shrimps inside our aquarium """

    all_shrimps = Shrimp.objects.order_by('birth_date').all()

    context = {
        "nb_shrimps": len(all_shrimps),
        "all_shrimps": all_shrimps
    }

    return render(request, "shrimps/home.html", context)


def give_birth_to_shrimp(request):
    """ give birth to a random baby shrimp """

    baby_shrimp = Shrimp.objects.create(
        name=choice(["Gerardi", "Evi", "Eli", "Niki", "Pauli"]),
        color=choice([color_tuple[0] for color_tuple in Shrimp.shrimp_colors]),
        size=randint(1, 200),
        weight=randint(1, 400),
        is_farmed=bool(randint(0, 1)),
    )

    return render(request, "shrimps/detail.html", context={"shrimp": baby_shrimp, "created": True})


def shrimp_detail(request, shrimp_id):
    """ display detail of a particular shrimp """

    shrimp = get_object_or_404(Shrimp, id=shrimp_id)
    # shrimp = Shrimp.objects.get(id=shrimp_id)

    return render(request, "shrimps/detail.html", context={"shrimp": shrimp})
