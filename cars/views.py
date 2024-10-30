from cars.models import Car
from cars.forms import CarModelForm
from django.views.generic import ListView, CreateView, DetailView
# from django.shortcuts import render, redirect
# from django.views import View



# Create your views here.

# FUNCTION BASED VIEWS
# def cars_view(request):
#     # FILTRANDO POR ITEM (BRAND, MODEL) DA TABELA CARS
#     # cars = Car.objects.filter(brand='1')
#     # cars = Car.objects.filter(brand__name='Fiat')
#     # cars = Car.objects.filter(model__contains='camaro')
#     # cars = Car.objects.filter(model__icontains='camaro')
#     # cars = Car.objects.all()
#     # cars = Car.objects.all().order_by('-model')
    
#     cars = Car.objects.all().order_by('model')
#     search = request.GET.get('search')
#     if search:      
#         cars = cars.filter(model__icontains=search).order_by('model')    
#     return render(request, 'cars.html', {'cars': cars})

# CLASS BASED VIEWS 
# class CarsView(View):
#     def get(self, request):
#         cars = Car.objects.all().order_by('model')
#         search = request.GET.get('search')
#         if search:      
#             cars = cars.filter(model__icontains=search).order_by('model')    
#         return render(request, 'cars.html', {'cars': cars})

class CarsView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    
    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:      
            cars = cars.filter(model__icontains=search) 
        return cars

############################################################################################################################################################

# FUNCTION BASED VIEWS
# def new_car_view(request):
#     if request.method == 'POST':
#         new_car_form = CarModelForm(request.POST, request.FILES)        
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect ('cars_list')
#     else:
#         new_car_form = CarModelForm()
#     return render(request, 'new_car.html', {'new_car_form': new_car_form})

# CLASS BASED VIEWS 
# class NewCarView(View):
#     def get(self, request):
#         new_car_form = CarModelForm()
#         return render(request, 'new_car.html', {'new_car_form': new_car_form})
#     def post(self, request):
#         new_car_form = CarModelForm(request.POST, request.FILES)            
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect ('cars_list')    
#         return render(request, 'new_car.html', {'new_car_form': new_car_form})

class NewCarView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'
    
class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'