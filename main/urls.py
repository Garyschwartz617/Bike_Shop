from django.urls import path

from .views import homepage,rental,rental_id,rental_add,customer,customer_id,customer_add,vehicle,vehicle_id,vehicle_add
 
urlpatterns = [
    
    path('', homepage),
    path('rental',rental,name='rental'),
    path('rental/<int:num>',rental_id, name = 'rental_id'),
    path('rental/add', rental_add),
    path('customer',customer, name='customer'), 
    path('customer/<int:num>',customer_id,name = 'customer_id'),
    path('customer/add', customer_add),
    path('vehicle',vehicle, name = 'vehicle'),
    path('vehicle/<int:num>',vehicle_id, name = 'vehicle_id'),
    path('vehicle/add', vehicle_add),


]