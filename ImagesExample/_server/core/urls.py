from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name="index"),
    path("uploads/", view=views.file_upload, name="upload file")
]