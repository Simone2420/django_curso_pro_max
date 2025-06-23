from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("car-form", views.create_car, name="create_car"),
    path("view-cars", views.CarList.as_view(), name="view_cars")
]

