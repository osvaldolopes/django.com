from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm

# Create your views here.

def cars_view(request):
    # FILTRANDO POR ITEM (BRAND, MODEL) DA TABELA CARS
    # cars = Car.objects.filter(brand='1')
    # cars = Car.objects.filter(brand__name='Fiat')
    # cars = Car.objects.filter(model__contains='camaro')
    # cars = Car.objects.filter(model__icontains='camaro')
    # cars = Car.objects.all()
    # cars = Car.objects.all().order_by('-model')
    
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')
    if search:      
        cars = cars.filter(model__icontains=search).order_by('model')    
    return render(request, 'cars.html', {'cars': cars})

def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarForm(request.POST, request.FILES)
        print (new_car_form.data)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect ('cars_list')
    else:
        new_car_form = CarForm()
    return render(request, 'new_car.html', {'new_car_form': new_car_form})