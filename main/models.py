from django.db import models
import datetime
# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=80)
    address = models.CharField(max_length=80, default= '12 apple road')
    city = models.CharField(max_length=80)
    country = models.CharField(max_length=80)
    def __str__(self):
        return f' {self.first_name} {self.last_name}'







class VehicleType(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return f' {self.name}'
    

class VehicleSize(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return f' {self.name}'

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    cost = models.IntegerField()
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.PROTECT)
    def __str__(self):
        return f'{self.vehicle_size.name} {self.vehicle_type.name}'
 
    def is_rented(self):
        try:
            if self.rental_set.order_by('return_date').last().return_date.replace(tzinfo=None) < datetime.datetime.now():
              return True    
            else:
              return False
        except:
            return True     



        # try:
        #     if self.rental_set.last().return_date.replace(tzinfo=None) < datetime.datetime.now():
        #       return 'you can rent me'    
        #     else:
        #       return 'you can NOT rent me'
        # except:
        #     return 'you can rent me'      

class Rental(models.Model):
    rental_date = models.DateTimeField(auto_now_add=False)
    return_date = models.DateTimeField(auto_now_add=False)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    def rented_vehicle(self):
        return self.vehicle

class RentalRate(models.Model):
    daily_rate = models.IntegerField()
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.PROTECT)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.PROTECT)
