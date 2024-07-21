from django.urls import path
from .import views

# Admin panel

urlpatterns =[
    path('',views.AdminLogin.AdminLogin, name='adminlogin'),
    path('dashboard/',views.Dashboard.dashboard, name='dashboard'),
    path('mail/',views.Dashboard.email, name='mail'),
    path('mai_delete/<int:id>',views.Dashboard.delete, name='mail_delete'),
    path('Out/',views.Out.out, name='out'),
    path('booking_Event/',views.Booking.booking,name='book_event'),
    path("delete_Event/<int:id>",views.Delete_items.event_delete,name='delete_event'),
    path("remove_blog/<int:id>",views.Delete_items.Remove_Blog,name='remove_blog'),
    path('admin_blog/',views.Blogs.blogs,name='admin_blogs'),
    path('add_blog/',views.Blogs.add_blog,name='add_blog'),
    path('read_blog_blog/<int:id>',views.Blogs.read_blog,name='read_blog'),
    path('edit_blog/<int:id>',views.Blogs.edit_blog,name='edit_blog'),
    path('change_images/<int:id>',views.changeImage,name='change_image'),
    path('password_change/',views.Password_change,name='password_change'),
    path('myprofile?/',views.myprofile, name='my-profile'),
    path('edit_myprofile/<int:id>',views.edit_myprofile, name='edit_profile'),



]