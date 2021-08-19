from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.


def homepage(request):
   
    return render(request,'index.html')


def rental(request):
    x = Rental.objects.all().order_by('rental_date')
    return render (request, 'rental.html', {'rentals': x})

def rental_id(request,num):
    x = Rental.objects.get(id = num)
    return render (request, 'rental_id.html', {'rental': x})

def rental_add(request):
    
    if request.method == 'GET':
        form = RentalAdd()
        
    elif request.method == 'POST':
        form = RentalAdd(request.POST)
        if form.is_valid():
            
            Rental.objects.create(**form.cleaned_data) 

            # return redirect('index')
    return render(request, 'rental_add.html', {'form':form})
    
def customer(request):
    x = Customer.objects.all().order_by('last_name', 'first_name')
    return render (request, 'customer.html', {'customers': x})

def customer_id(request,num):
    x = Customer.objects.get(id = num)
    return render (request, 'customer_id.html', {'customer': x})

def customer_add(request):
    
    if request.method == 'GET':
        form = CustomerAdd()
        
    elif request.method == 'POST':
        form = CustomerAdd(request.POST)
        if form.is_valid():
            
            Customer.objects.create(**form.cleaned_data) 

            # return redirect('index')
    return render(request, 'customer_add.html', {'form':form})

def vehicle(request):
    x = Vehicle.objects.all().order_by('vehicle_type','vehicle_size')
    return render (request, 'vehicle.html', {'vehicles': x})

def vehicle_id(request,num):
    x = Vehicle.objects.get(id = num)
    return render (request, 'vehicle_id.html', {'vehicle': x})

def vehicle_add(request):
    
    if request.method == 'GET':
        form = VehicleAdd()
        
    elif request.method == 'POST':
        form = VehicleAdd(request.POST)
        if form.is_valid():
            
            Vehicle.objects.create(**form.cleaned_data) 

            # return redirect('index')
    return render(request, 'vehicle_add.html', {'form':form})


# rent_id,rental_add,customer,customer_id,customer_add,vehicle,vehicle_id,vehicle_add