from django.urls import path

from shrimps.views import home, give_birth_to_shrimp, detail


app_name = 'shrimps'
urlpatterns = [
    path('', home, name="home"),  # default path (null) so doesn't need any path string
    path('give-birth', give_birth_to_shrimp, name="give-birth"),
    path('<int:shrimp_id>/detail', detail, name="detail"),
]
