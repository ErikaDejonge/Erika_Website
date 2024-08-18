from django.contrib import admin
from .models import Country,Profile_Images,Receive_Contact
# Register your models here.
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id','city_name']

@admin.register(Profile_Images)
class Profile_ImagesAdmin(admin.ModelAdmin):
    list_display =['id','profile_Image']

@admin.register(Receive_Contact)
class Receive_ContactAdmin(admin.ModelAdmin):
    list_display=['id','Name','Email','Messages']