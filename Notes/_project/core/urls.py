from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index),
    path("notes/", view=views.notes)
]