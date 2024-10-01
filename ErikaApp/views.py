from django.shortcuts import render,redirect
from .models import Blog,BookErika,Email_Info,Download_email
from django.core.paginator import Paginator
from django.contrib import messages
from Erika_Admin.models import Receive_Contact,AboutMe,Books,Reviews
from .utlis import send_email_with_attachment
from django.conf import settings
from django.http import HttpResponse

# Create your views here.

# 404 Error start
def handling_404(request, exception):
    return render(request, '404.html', {})

def base(request):
    return render(request, 'main/base.html')

# 404 Error ends

def index(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 4)
    page_number = request.GET.get('page')
    blog = paginator.get_page(page_number)

    context = {
        'blog': blog
    }
    return render(request,  'main/index.html',context)

def blog(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 4)
    page_number = request.GET.get('page')
    pg_blogs = paginator.get_page(page_number)

    blog_content  = Blog.objects.all()
    get_blog_content = Paginator(blog_content,4)
    page_number =request.GET.get('page')
    obj_blog = get_blog_content.get_page(page_number)

# collection of the context
    context = {
        'blogs': blogs,
        'pg_blogs': pg_blogs,
        'blog_content':obj_blog

    }
    return render(request, 'main/blog.html',context)

def showBlog(request,id):
    blog = Blog.objects.get(id=id)


# to show the blog title in the blog page 
    blog_content  = Blog.objects.all()
    get_blog_content = Paginator(blog_content,4)
    page_number = request.GET.get('page')
    obj_blog = get_blog_content.get_page(page_number)

    context ={
        'show_blog': blog,
        'blog_content':obj_blog
    }

    return render(request, 'main/showblog.html',context)

class Book():
    def book(request):
        if request.method == 'POST':
            Name = request.POST['name']
            Event_description = request.POST['event_description']
            Email = request.POST['email']
            Phone = request.POST['phone']
            try:
                if Email != BookErika.objects.filter(Email=Email).exists():
                    book_info = BookErika(Name=Name,EventDescription=Event_description, Email=Email,Phone=Phone)
                    book_info.save()
                    return redirect('index')
            except:
                messages.warning(request, 'This Email Already Exit')
                return redirect('index')
        

    def info_Email(request):
        if request.method =='POST':
            News_Email = request.POST['News_Mail']

            Info_Email = Email_Info(Info_Email  = News_Email )
            Info_Email.save()
            return redirect('index')

class Tools():
    def tools(request):

        if request.method == 'POST':
            email_send = request.POST['email']
            sv_e = Download_email(Downloaded_Email=email_send)
            sv_e.save()

            subject= 'With file attachment: from the Erika Books'
            message= 'Download the Files'
            recipient_list = [email_send]
            file_path = f'{settings.BASE_DIR}/planner.pdf'
            send_email_with_attachment(subject, message, recipient_list, file_path)
            return redirect('tools')


        return render(request, "main/tools.html")
    
class About():
    def about(request):
        about_show = AboutMe.objects.all()
        return render(request, "main/about.html",{'about_show':about_show})
    
class ReadBooks():
    def books(request):
        show_books = Books.objects.all()
        show_reviews = Reviews.objects.all()
        context={
            'show_books':show_books,
            'show_reviews':show_reviews
        }
        return render(request, "main/book.html",context)
    
class Contact():
    def contact(request):
        if request.method =='POST':
            name = request.POST['name']
            email = request.POST['email']
            message =  request.POST['message']
            RegisterContact = Receive_Contact(Name=name, Email= email, Messages = message)
            RegisterContact.save()
            messages.success(request, "We've received your message and will follow up shortly.")
            return redirect('contact')
        return render(request,  'main/contact.html')
    
