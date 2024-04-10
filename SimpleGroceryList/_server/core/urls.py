from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name="index"),
    path('grocery_lists/', views.grocery_lists, name="grocery_lists"),
    path('grocery_lists/<int:id>/', view=views.grocery_list, name="get list"),
    path('grocery_lists/<int:id>/items/<int:item_id>/', view=views.update_item, name="update item")
]