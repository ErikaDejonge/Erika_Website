from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from ErikaApp.models import Email_Info,BookErika,Blog
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.core.paginator import Paginator
from django.urls import reverse_lazy,reverse
from django.forms import forms

# Create your views here.

def admin_Login(request):
    if request.user.is_authenticated:
        return redirect('erika-dashboard')
    
    if request.method =='POST':
        username = request.POST['username']
        password =request.POST['password']

        Admin_user = User.objects.filter(username=username)
        if not Admin_user.exists():
            messages.info(request, f'Hey \'{username}\' your are not a Admin manager Please visit the site..')
            return redirect('admin-sign-in')
        
        Admin_user = authenticate(username=username, password=password)
        if Admin_user is not None and Admin_user.is_superuser:
            login(request, Admin_user)
            return redirect('erika-dashboard')
        
        messages.info(request, 'Invalid Password')
        return redirect('admin-sign-in')
    
    return render(request,  'main/login.html')

@login_required(login_url='admin-sign-in')
def sign_out(request):
    logout(request)
    return redirect('admin-sign-in')


@login_required(login_url='admin-sign-in')
def dashboard(request):
    blog = Blog.objects.all()
    context = {
        'blog':blog,
        }
    return render(request, 'main/dashboard.html',context)

#  main pages source code

@login_required(login_url='admin-sign-in')
def book_erika(request):
    event_book = BookErika.objects.all()
    context = {
        'event_book':event_book,
    }
    return render ( request, 'pages/Bookings/book_erika.html',context)

@login_required(login_url='admin-sign-in')
def email(request):

    all_mail = Email_Info.objects.all()
    context = {
        'all_email':all_mail
    }
    return render(request, 'pages/Email/Email.html',context)

@login_required(login_url='admin-sign-in')
class Delete_element():
    def mail_remove(request, id):
        mail = Email_Info.objects.get(id=id)
        mail.delete()
        messages.success(request, f'{mail} Deleted Successfully')
        return redirect('email')

def form(request):
    return render(request, 'pages/forms/form.html')


def blog(request):
    return render(request, 'pages/blogs/blog.html')

#@login_required(login_url='admin-login')
# def Delete_User_Admin(request):
#     User.objects.get(username = request, is_superuser = True).delete()
#     return redirect('admin-login')

    

# class Dashboard():
#     @login_required(login_url='admin-login')
#     def dashboard(request):
#         blogs = Blog.objects.all()
#         context={
#             'blogs':blogs,
#         }
#         return render(request, 'main/dashboard.html',context)
    
#     @login_required(login_url='admin-login')
#     def email(request):
#         mail = Email_Info.objects.all()

#         context = {
#             'mail':mail,

#         }
#         return render(request, 'main/mail.html',context)
    
#     @login_required(login_url='admin-login')
#     def delete(request,id):
#         mail_delete = Email_Info.objects.get(id=id)
#         mail_delete.delete()
#         return redirect('mail')

# class Delete_items():
#     @login_required(login_url='admin-login')
#     def event_delete(request,id):
#         event = BookErika.objects.get(id=id)
#         event.delete()
#         return redirect('book_event')
    
#     @login_required(login_url='admin-login')
#     def Remove_Blog(request,id):
#         remove= Blog.objects.get(id=id)
#         remove.delete()
#         return redirect('admin_blogs')
    
#     @login_required(login_url='admin-login')
#     def add_blog(request):
#         if request.method == 'POST' and request.FILES:
#             title = request.POST['title']
#             introduction = request.POST['introduction']
#             paragraph = request.POST['paragraph']
#             image = request.FILES['image']
#             blog = Blog(blog_title=title, blog_intro=introduction, blog_body=paragraph, image=image)
#             blog.save()
#             messages.info(request, 'Blog Added Successfully')
#             return redirect('admin_blogs')
#         return render(request, 'main/add_blog.html')
    
#     @login_required(login_url='admin-login')
#     def read_blog(request,id):
#         read = Blog.objects.get(id=id)
#         context ={
#             'read':read,                    
#         }
#         return render(request, 'main/read_blog.html',context )
    
#     @login_required(login_url='admin-login')
#     def edit_blog(request,id):
#         if request.method=="POST":
#             edit=Blog.objects.get(id=id)
#             edit.blog_title = request.POST['title']
#             edit.blog_intro = request.POST['introduction']
#             edit.blog_body = request.POST['paragraph']
#             # edit.image = request.FILES['image']
#             edit.save()
#             messages.info(request, 'Blog Updated Successfully')
#             return redirect('admin_blogs')            
            
#         edit_blog = Blog.objects.get(id=id)
#         context ={
#             'edit_blog':edit_blog,                    
#         }
#         return render(request, 'main/edit_blog.html',context)
# @login_required(login_url='admin-login')
# def changeImage(request, id):
#     if request.FILES and  request.method=="POST":
#         new_img = Blog.objects.get(id=id)
#         new_img.image = request.FILES['new_image']
#         new_img.save()
#         messages.info(request, 'Image Updated Successfully')
#         return redirect('admin_blogs')
    
#     old_image = Blog.objects.get(id=id)
#     context={
#         'old_image':old_image,
#     }
#     return render(request, 'main/change_image.html',context)
    
# # class PasswordChangingView(PasswordChangeView):
# #     form_class = Password_Change_Form
# #     success_url = reverse_lazy('password_change_success')

# # def password_success(request):
# #     return render(request, 'password/password_change_success.html')

# # Change password
# @login_required(login_url='admin-login')
# def Password_change(request):
#     if request.method == 'POST':
#         fm = PasswordChangeForm(user=request.user, data=request.POST)
#         if fm.is_valid():
#             fm.save()
#             update_session_auth_hash(request,fm.user)
#             messages.success(request, 'Password is change successfully')
#             return redirect('dashboard')

        
#         messages.error(request, 'Re-enter or Check the password correctly')
#         return redirect('password_change')    

#     else:
#         fm = PasswordChangeForm(user=request.user)
#     return render(request, 'password/password_change.html',{'fm':fm})