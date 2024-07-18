from django.contrib import admin
from .models import Blog, BookErika,Email_Info

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','blog_title', 'blog_intro', 'blog_body', 'image')

@admin.register(BookErika)
class BookErikaAdmin(admin.ModelAdmin):
    list_display = ['id','Name','EventDescription','Email','Phone']

@admin.register(Email_Info)
class Email_InfoAdmin(admin.ModelAdmin):
    list_display= ['id','Info_Email']