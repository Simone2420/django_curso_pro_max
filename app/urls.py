from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("car-form", views.create_car, name="create_car"),
    path("view-cars", views.view_cars, name="view_cars")
]

