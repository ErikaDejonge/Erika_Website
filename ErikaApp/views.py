from django.shortcuts import render,redirect
from .models import Blog,BookErika,Email_Info
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.

# 404 Error start
def handling_404(request, exception):
    return render(request, '404.html', {})

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
    paginator = Paginator(blogs, 1)
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
        "blog": blog,
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
                        book_info = BookErika(Name=Name,EventDescription=Event_description, Email =Email,Phone=Phone)
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
        return render(request, "main/tools.html")
    
class About():
    def about(request):
        return render(request, "main/about.html")
    
class Books():
    def books(request):
        return render(request, "main/book.html")
    
class Contact():
    def contact(request):
        return render(request,  'main/contact.html')