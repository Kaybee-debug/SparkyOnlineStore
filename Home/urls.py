from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name="index"),
    path("add/",views.add_product,name="add"),
     path("product/<pk>/edit/",views.update,name="edit"),
        path("product/<pk>/delete/",views.delete,name="delete"),
     
]