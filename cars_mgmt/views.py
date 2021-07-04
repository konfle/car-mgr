from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Car
from .forms import CarForm


def show_all_cars(request):
    all_cars = Car.objects.all()
    return render(request, 'cars.html', {'cars': all_cars})


def show_car_by_id(request, id):
    car = get_object_or_404(Car, pk=id)
    return render(request, 'car_details.html', {'car': car})


@login_required
def new_car(request):
    form_car = CarForm(request.POST or None)
    template_name = 'car_form.html'

    if form_car.is_valid():
        form_car.save()
        return redirect(show_all_cars)

    return render(request, template_name, {'form_car': form_car, 'new': True})


@login_required
def edit_car(request, id):
    template_name = 'car_form.html'
    car = get_object_or_404(Car, pk=id)
    form = CarForm(request.POST or None, instance=car)

    if form.is_valid():
        form.save()
        return redirect(show_all_cars)

    return render(request, template_name, {'form_car': form, 'new': False})


@login_required
def delete_car(request, id):
    template_name = 'delete_car.html'
    car = get_object_or_404(Car, pk=id)

    if request.method == 'POST':
        car.delete()
        return redirect(show_all_cars)

    return render(request, template_name, {'car': car, 'remove': False})


@login_required
def show_car_by_plate(request, registration_number):
    car = get_object_or_404(Car, registration_number=registration_number)
    return render(request, 'car_details.html', {'car': car, 'remove': True})
