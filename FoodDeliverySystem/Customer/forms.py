from django import forms
from Customer.models import Customer


class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
