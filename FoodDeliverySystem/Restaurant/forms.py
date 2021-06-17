from django import forms
from .models import Restaurant


class RestaurantDetailsForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'
        exclude = ['user']
