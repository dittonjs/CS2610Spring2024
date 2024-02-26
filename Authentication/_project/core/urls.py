from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", view=views.index),
    path("dashboard/", view=views.dashboard),
]
