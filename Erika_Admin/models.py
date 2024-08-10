from django.db import models

# Create your models here.

class Country(models.Model):
    city_name = models.CharField(max_length=100, default='kathmandu')


    def __str__(self):
        return self.city_name

class Profile_Images(models.Model):
    profile_Image = models.ImageField(upload_to='ProfileImg')

    