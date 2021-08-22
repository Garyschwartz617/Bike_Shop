from django import forms
from .models import *

class RentalAdd(forms.Form):
    rental_date = forms.DateTimeField()
    return_date = forms.DateTimeField()
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.all())
        
class CustomerAdd(forms.Form):

    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.CharField(max_length=80)
    phone_number = forms.CharField(max_length=80)
    address = forms.CharField(max_length=80)
    city = forms.CharField(max_length=80)
    country = forms.CharField(max_length=80)

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
    first_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'placeholder': 'Write your first name here','title': 'Search'
            })
        )    
    email = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'placeholder': 'Write your email here'
            })
        )    


class VehicleAdd(forms.Form):

    vehicle_size = forms.ModelChoiceField(queryset=VehicleSize.objects.all())
    vehicle_type = forms.ModelChoiceField(queryset=VehicleType.objects.all())
    cost = forms.IntegerField()

