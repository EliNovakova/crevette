from django.utils import timezone

from shrimps.models import Shrimp

s = Shrimp(name="Paul", weight=50, size=40, color="rainbow", is_farmed=False)
s.save()

print(s.weight, s.id, s.color, s.birth_date)
print(s)

s = Shrimp.objects.create(name="Gerard", weight=50, size=40, color="black")
print(s.weight, s.id, s.color, s.birth_date)
print(s)
