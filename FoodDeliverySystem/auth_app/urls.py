from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import CustomerRegisterForm, RestaurantRegisterForm, LoginForm
from Customer.forms import CustomerDetailsForm
from Restaurant.forms import RestaurantDetailsForm
from .views import FormWizardView
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/',
         FormWizardView.as_view([CustomerRegisterForm, CustomerDetailsForm]), name="register"),
    path('login/', auth_views.LoginView.as_view(form_class=LoginForm,
         template_name='auth_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
