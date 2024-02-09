from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index),
    path("notes/", view=views.create_note),
    path("notes/<id>/", view=views.show_note),
    path("notes/<id>/tasks/", view=views.create_task),
    path("delete_note/<id>/", view=views.delete_note),
    path("tasks/<id>/", view=views.update_task)
]
