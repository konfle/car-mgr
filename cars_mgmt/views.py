from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
from .forms import CarForm


def show_all_cars(request):
    all_cars = Car.objects.all()
    return render(request, 'cars.html', {'cars': all_cars})


def new_car(request):
    form_car = CarForm(request.POST or None)
    template_name = 'car_form.html'

    if form_car.is_valid():
        form_car.save()
        return redirect(show_all_cars)

    return render(request, template_name, {'form_car': form_car, 'new': True})


def edit_car(request, id):
    template_name = 'car_form.html'
    car = get_object_or_404(Car, pk=id)
    form = CarForm(request.POST or None, instance=car)

    if form.is_valid():
        form.save()
        return redirect(show_all_cars)

    return render(request, template_name, {'form_car': form})


def delete_car(request, id):
    template_name = 'delete_car.html'
    car = get_object_or_404(Car, pk=id)

    if request.method == 'POST':
        car.delete()
        return redirect(show_all_cars)

    return render(request, template_name, {'car': car})


def show_car_by_id(request, id):
    car = get_object_or_404(Car, pk=id)
    return render(request, 'car_details.html', {'car': car})


def show_car_by_plate(request, registration_number):
    car = get_object_or_404(Car, registration_number=registration_number)
    return render(request, 'car_details.html', {'car': car})
