from faker import Faker
import os
import django
import random


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike.settings')
django.setup()

from main.models import *

def make_first_name():
    fake = Faker()
    return fake.first_name()

def make_last_name():
    fake = Faker()
    return fake.last_name()

def make_email():
    fake = Faker()
    return fake.ascii_email()

def make_phone_number():
    fake = Faker()
    return fake.phone_number()

def make_address():
    fake = Faker()
    return fake.address()

def make_city():
    fake = Faker()
    return fake.city()

def make_country():
    fake = Faker()
    return fake.country()

def make_customer(num):
    for i in range(num):
        Customer.objects.create( first_name = make_first_name(), last_name = make_last_name(), email = make_email(), phone_number = make_phone_number(),address = make_address(), city = make_city(),country = make_country()
) 

def make_vehicle_type():
    lst = ['scooter','bike','jetpack','electrice bike']
    for item in lst:
        VehicleType.objects.create(name = item)
   
    # x = random.choice([])
def make_vehicle_size():
    lst = ['large','medium','small']
    for item in lst:
        VehicleSize.objects.create(name = item)

def make_vehicle(num):
    for i in range(num):
        x = random.choice(VehicleType.objects.all())
        y = random.choice(VehicleSize.objects.all())
        z = random.randrange(50, 500)
        Vehicle.objects.create(vehicle_type= x, vehicle_size = y, cost = z)


def make_date():
    fake = Faker()
    return fake.date()

def make_rental(num):
    for i in range(num):
        x = random.choice(Vehicle.objects.all())
        y = random.choice(Customer.objects.all())
        z = make_date()
        t = make_date()
        if  z >t:
            early = t
            late = z
        else:
            early = z
            late = t    
        Rental.objects.create(customer= y, vehicle = x, rental_date = early, return_date =late)



def make_rental_rate():

    for i in VehicleType.objects.all():
        for y in VehicleSize.objects.all():
            z = random.randrange(5, 50)
            RentalRate.objects.create(vehicle_type= i, vehicle_size = y, daily_rate  = z)

    # for i in range(num):
    #     x = random.choice(VehicleType.objects.all())
    #     y = random.choice(VehicleSize.objects.all())
    #     z = random.randrange(5, 50)
    #     RentalRate.objects.create(vehicle_type= x, vehicle_size = y, daily_rate  = z)


