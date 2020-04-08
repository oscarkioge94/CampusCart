from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name','identification_number', 'phone_number','registration_number', 'email',
                   'place_of_residence' , 'room_number'
                  ]
