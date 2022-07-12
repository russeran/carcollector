from black import List
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic import DetailView
from . models import Car

# Create your views here.
#define home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
    
def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})



def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/detail.html', {'car': car})

# class CarDetail(DetailView):
#     model = Car
#     template_name = 'cars/detail.html'
  


class CarCreate(CreateView):
    model = Car
    fields = '__all__'
    
class CarUpdate(UpdateView):
    model = Car
    fields = '__all__'

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'        