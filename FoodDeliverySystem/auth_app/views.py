import os
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import CustomerRegisterForm, RestaurantRegisterForm, LoginForm
from Customer.forms import CustomerDetailsForm
from Restaurant.forms import RestaurantDetailsForm
from Customer.models import Customer
from Restaurant.models import Restaurant
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from formtools.wizard.views import SessionWizardView


def home(request):
    return render(request, 'auth_app/home.html')


class FormWizardView(SessionWizardView):
    template_name = "auth_app/register.html"
    form_list = [CustomerRegisterForm, CustomerDetailsForm]
    file_storage = FileSystemStorage(location=os.path.join(
        settings.MEDIA_ROOT, 'images/profile_pics'))

    def done(self, form_list, form_dict, **kwargs):
        register_form = form_dict['0'].cleaned_data
        detail_form = form_dict['1'].cleaned_data
        user = self.create_user(register_form)
        self.create_customer(detail_form, user)
        return redirect('login')

    def create_user(self, register_form):
        user = User(
            username=register_form['username'],
            email=register_form['email'],
        )
        user.set_password(register_form['password1'])
        user.save()
        return user

    def create_customer(self, detail_form, user):
        customer = Customer(
            user=user,
            first_name=detail_form['first_name'],
            last_name=detail_form['last_name'],
            phone=detail_form['phone'],
            address=detail_form['address'],
            profile_pic=detail_form['profile_pic'],
        )
        customer.save()
