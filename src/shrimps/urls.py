from django.urls import path

from shrimps.views import home, give_birth_to_shrimp


urlpatterns = [
    path('', home, name="home"),
    path('give-birth/', give_birth_to_shrimp, name="give-birth")
]
