from django.urls import path

from shrimps.views import home, give_birth_to_shrimp, shrimp_detail, edit_shrimp
app_name = "shrimps"

urlpatterns = [
    path('', home, name="home"),  # default path (null) so doesn't need any path string
    path('give-birth/', give_birth_to_shrimp, name="give-birth"),
    path('<int:shrimp_id>/detail/', shrimp_detail, name="detail"),
    path('<int:shrimp_id>/edit/', edit_shrimp, name="edit"),
    path('create/', edit_shrimp, name="create"),
]
