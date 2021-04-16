from django.urls import path

from shrimps.views import home

urlpatterns = [
    path('', home, name="home"),
]
