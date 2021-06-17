from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User


class Restaurant(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    resto_name = models.CharField(max_length=50, null=True)
    resto_phone = models.CharField(max_length=50, null=True)
    resto_address = models.CharField(max_length=50, null=True)
    resto_pic = models.ImageField(
        default='profile1.png', upload_to='static/images/resto_pics/')

    def __str__(self):
        return self.resto_name

    def save(self, *args, **kwargs):
        super(Restaurant, self).save(*args, **kwargs)
