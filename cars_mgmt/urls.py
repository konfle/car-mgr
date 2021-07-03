from django.contrib import admin
from django.urls import path, include
from .views import show_all_cars, new_car, edit_car, delete_car, show_car_by_id, show_car_by_plate

urlpatterns = [
    path('all/', show_all_cars, name="all_cars"),
    path('new/', new_car, name="new_car"),
    path('edit/<int:id>', edit_car, name="edit_car"),
    path('delete/<int:id>', delete_car, name="delete_car"),
    path('car/<int:id>', show_car_by_id, name="show_car"),
    path('plate/<str:registration_number>', show_car_by_plate, name="show_car_plate"),
]
