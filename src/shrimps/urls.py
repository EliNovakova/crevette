from django.urls import path

from shrimps.views import home, give_birth_to_shrimp, shrimp_detail

app_name = "shrimps"

urlpatterns = [
    path('', home, name="home"),
    path('give-birth/', give_birth_to_shrimp, name="give-birth"),
    path('<int:shrimp_id>/dkdkd/dozejfoziefj/', shrimp_detail, name="detail")
]
