from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_htm, name="index_htm"),
    path("brian", views.greet_brian, name="greet_brian"),
    path("david", views.greet_david, name="greet_david"),
    path("<str:name_in_url>", views.greet_htm, name="greet_htm")
]