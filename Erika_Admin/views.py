from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from ErikaApp.models import Email_Info,BookErika,Blog
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profile_Images
import requests
import json
from django.contrib import messages
import datetime
import os




# Create your views here.
def profiles(request):
    account = Profile_Images.objects.all()
    context = {
        'account':account
    }
    return render(request, 'partials/base.html',context)

class AdminLogin():
    def AdminLogin(request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        if request.method =='POST':
            username = request.POST.get('username')
            password =request.POST['password']

            Admin_user = User.objects.filter(username=username)
            if not Admin_user.exists():
                messages.info(request, f'Hey \'{username}\' your are not a Admin manager Please visit the site..')
                return redirect('adminlogin')
            
            Admin_user = authenticate(username=username, password=password)
            if Admin_user is not None and Admin_user.is_superuser:
                login(request, Admin_user)
                messages.info(request,f"{username} Welcome Back to Management System")
                return redirect('dashboard')
            messages.info(request, 'Invalid Password')
            return redirect('adminlogin')

        return render(request,  'main/login.html')
    
@login_required(login_url='adminlogin')
def myprofile(request):
    
    return render(request, 'profile/myprofile.html')   

@login_required(login_url='adminlogin')
def edit_myprofile(request,id):
    if request.method == 'POST':
        adu = User.objects.get(id=id)
        adu.username = request.POST['username']
        adu.email = request.POST['email']
        adu.save()
        messages.success(request, 'User name and Email address is updated successfully..')
        return redirect('my-profile')


    adu =  User.objects.get(id=id)
    context = {
        'adu':adu
    }
    return render(request, 'profile/Edit_profile.html',context)    


class Out():
    @login_required(login_url='adminlogin')
    def out(request):
        logout(request)
        return redirect('adminlogin')
    
    @login_required(login_url='adminlogin')
    def Delete_User_Admin(request):
        User.objects.get(username = request, is_superuser = True).delete()
        return redirect('adminlogin')

class Dashboard():
    @login_required(login_url='adminlogin')
    def dashboard(request):
        # weather start     
        city = 'Kathmandu'    
        url =f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bf22686cf11682e29d657b984d138978'
        PARAMS = {"units":"metric"}

        data = requests.get(url, PARAMS).json()

        temp = data["main"]['temp']       
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        description = data['weather'][0]['description']
        cloud = data['clouds']['all']
        
            
        blogs = Blog.objects.all()
        context={
            'blogs':blogs,

            'city':city,
            'temp':temp,
            'humidity':humidity,
            'wind':wind,
            'description':description,
            'cloud':cloud,                
            'time':datetime.datetime.now(),
            "dt":datetime.datetime.now()

        }
        return render(request, 'main/dashboard.html',context)
    
    @login_required(login_url='adminlogin')
    def email(request):
        mail = Email_Info.objects.all()

        context = {
            'mail':mail,

        }
        return render(request, 'main/mail.html',context)
    
    @login_required(login_url='adminlogin')
    def delete(request,id):
        mail_delete = Email_Info.objects.get(id=id)
        mail_delete.delete()
        return redirect('mail')
        
class Booking():
    @login_required(login_url='adminlogin')
    def booking(request):
        event_book = BookErika.objects.all()
        context = {
            'event_book':event_book,
            }
        return render(request, 'main/admin_book.html',context)

class Delete_items():
    @login_required(login_url='adminlogin')
    def event_delete(request,id):
        event = BookErika.objects.get(id=id)
        event.delete()
        return redirect('book_event')
    
    @login_required(login_url='adminlogin')
    def Remove_Blog(request,id):
        remove_blog= Blog.objects.get(id=id)
        if len(remove_blog.image)>0:
            os.remove(remove_blog.image.path)
        remove_blog.delete()
        return redirect('admin_blogs')


class Blogs():
    @login_required(login_url='adminlogin')
    def blogs(request):
        blog = Blog.objects.all()
        context = {
            'blog':blog,
            }
        return render(request, 'main/admin_blog.html',context)
    
    @login_required(login_url='adminlogin')
    def add_blog(request):
        if request.method == 'POST' and request.FILES:
            title = request.POST['title']
            introduction = request.POST['introduction']
            paragraph = request.POST['paragraph']
            image = request.FILES['image']
            blog = Blog(blog_title=title, blog_intro=introduction, blog_body=paragraph, image=image)
            blog.save()
            messages.info(request, 'Blog Added Successfully')
            return redirect('admin_blogs')
        return render(request, 'main/add_blog.html')
    
    @login_required(login_url='adminlogin')
    def read_blog(request,id):
        read = Blog.objects.get(id=id)
        context ={
            'read':read,                    
        }
        return render(request, 'main/read_blog.html',context )
    
    @login_required(login_url='adminlogin')
    def edit_blog(request,id):
        if request.method=="POST":
            edit=Blog.objects.get(id=id)
            edit.blog_title = request.POST['title']
            edit.blog_intro = request.POST['introduction']
            edit.blog_body = request.POST['paragraph']
            # edit.image = request.FILES['image']
            edit.save()
            messages.info(request, 'Blog Updated Successfully')
            return redirect('admin_blogs')            
            
        edit_blog = Blog.objects.get(id=id)
        context ={
            'edit_blog':edit_blog,                    
        }
        return render(request, 'main/edit_blog.html',context)
@login_required(login_url='adminlogin')
def changeImage(request, id):
    if request.FILES and  request.method=="POST":
        new_img = Blog.objects.get(id=id)
        new_img.image = request.FILES['new_image']
        new_img.save()
        messages.info(request, 'Image Updated Successfully')
        return redirect('admin_blogs')
    
    old_image = Blog.objects.get(id=id)
    context={
        'old_image':old_image,
    }
    return render(request, 'main/change_image.html',context)
    
# class PasswordChangingView(PasswordChangeView):
#     form_class = Password_Change_Form
#     success_url = reverse_lazy('password_change_success')

# def password_success(request):
#     return render(request, 'password/password_change_success.html')

# Change password
@login_required(login_url='adminlogin')
def Password_change(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            messages.success(request, 'Password is change successfully')
            return redirect('dashboard')

        
        messages.error(request, 'Re-enter or Check the password correctly')
        return redirect('password_change')    

    else:
        fm = PasswordChangeForm(user=request.user)
    return render(request, 'password/password_change.html',{'fm':fm})

def profile_image(request):
    if request.method=='POST' and request.FILES:
        profile_img = request.FILES['profile_image']
        profileimage = Profile_Images(profile_Image = profile_img)
        profileimage.save()
        return redirect('my-profile')

    return render(request, 'profile/image.html')