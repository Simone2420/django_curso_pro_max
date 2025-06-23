from django.shortcuts import render, redirect
from app.models import Car
from django.views.generic.base import TemplateView

# Create your views here.
def index(request):
    return render(request, "index.html", {
        "title": "Home",
        "content_page": "Welcome to my home page!"
    })
    
def create_car(request):
    if request.method == "POST":
        name = request.POST["name"]
        color = request.POST["color"]
        car = Car(name=name, color=color)
        car.save()
        return redirect("view_cars")
    return render(request, "car_form.html", {
            "title": "Car Form"
        })
    
def view_cars(request):
    cars = Car.objects.all()
    return render(request, "view_cars.html", {
        "title": "View Cars",
        "cars": cars
    })
def delete_car(request, car_id):
    car = Car.objects.get(id=car_id)
    car.delete()
    return redirect("view_cars")
def update_car(request, car_id):
    car = Car.objects.get(id=car_id)
    if request.method == "POST":
        car.name = request.POST["name"]
        car.color = request.POST["color"]
        car.save()
        return redirect("view_cars")
    return render(request, "car_form.html", {
        "title": "Update Car",
        "car": car
    })
class CarList(TemplateView): 
    template_name = "view_cars.html"
    def get_context_data(self):
        carlist = Car.objects.all()
        context = {
            "cars": carlist
        }
        return context
