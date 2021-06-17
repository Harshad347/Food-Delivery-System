from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    profile_pic = models.ImageField(
        default='profile1.png', upload_to='static/images/profile_pics/')

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)
