
from secrets import token_bytes
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Car, Website
from .forms import CommentForm

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
    form = CommentForm()
    website_ids = car.websites.all().values_list('id')
    websites = Website.objects.exclude(id__in=website_ids)
    return render(request, 'cars/detail.html', {'form': form,
     'car': car,
    'websites': websites})
    

# class CarDetail(DetailView):
#     model = Car
#     template_name = 'cars/detail.html'
  
class CarCreate(CreateView):
    model = Car
    fields = ['name', 'make', 'model', 'year', 'price']
    
class CarUpdate(UpdateView):
    model = Car
    fields = ['make', 'model', 'year']

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'   

def add_comment(request, car_id):
    
  
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.car_id = car_id
        new_comment.save()
    return redirect('detail', car_id=car_id)
    

class WebsiteList(ListView):
    model = Website

class WebsiteDetail(DetailView):
    model = Website

class WebsiteCreate(CreateView):
    model = Website
    fields = ['name', 'link']

class WebsiteUpdate(UpdateView):
    model = Website
    fields = ['name', 'link']

class WebsiteDelete(DeleteView):
    model = Website
    success_url = '/websites/'                 

def assoc_website(request, car_id, website_id):
    car = Car.objects.get(id=car_id)
    car.websites.add(website_id)
    return redirect('detail', car_id=car_id) 

def unassoc_website(request, car_id, website_id):
    car = Car.objects.get(id=car_id)
    car.websites.remove(website_id)
    return redirect('detail', car_id=car_id) 