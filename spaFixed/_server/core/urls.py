from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name="index"),
    path('me/', view=views.me, name="me")
]