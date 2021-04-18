from random import randint, choice

from django.http import HttpResponse

from shrimps.models import Shrimp


def home(request):
    """ home page: display the numbers of shrimps inside our aquarium """

    nb_shrimps = Shrimp.objects.count()
    # SELECT COUNT(*) FROM shrimp;
    # nb_shrimps = len(Shrimp.objects.all())
    # SELECT * FROM shrimp;

    content = f"""There are {nb_shrimps} shrimps in our aquarium."""

    last_shrimp = Shrimp.objects.order_by('birth_date').last()
    if last_shrimp is not None:
        content += f""" The last shrimp born is {last_shrimp}."""

    return HttpResponse(content)


def give_birth_to_shrimp(request):
    """ give birth to a random baby shrimp """

    baby_shrimp = Shrimp.objects.create(
        name=choice(["Gerardi", "Evi", "Eli", "Niki", "Pauli"]),
        color=choice([color_tuple[0] for color_tuple in Shrimp.shrimp_colors]),
        size=randint(1, 200),
        weight=randint(1, 400),
        is_farmed=bool(randint(0, 1)),
    )

    return HttpResponse(f"""A new baby shrimp named {baby_shrimp.name} is born and weighs
                        {baby_shrimp.weight} grams and measures {baby_shrimp.size} mm.""")
