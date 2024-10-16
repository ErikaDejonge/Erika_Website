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
    path('profile=img/',views.profile_image,name='profile-image'),
    path('receive-contact/', views.Receive_Contacts.receive_contacts,name='admin-contacts'),
    path('RC_Delete/<int:id>',views.Receive_Contacts.RC_Delete,name='RC_delete'),
    path('aboutMe/',views.aboutme, name='about-me'),
    path('add_aboutMe/',views.add_about_content, name='add-about-content'),
    path('edit_aboutMe/<int:id>',views.edit_about_content, name='edit-about-content'),
    path('change_image/<int:id>',views.change_about_image, name='change_about_image'),
    path('delete_aboutMe/<int:id>',views.delete_about_content, name='delete-about-content'),

    path('book-sections/',views.books_sections, name='books-section'),
    path('edit-book-sections/<int:id>',views.edit_books_sections, name='edit_books-section'),
    path('edit_books_image_section/<int:id>',views.edit_books_image_section,name='edit_books_image_sections'),
    path('delete_books/<int:id>',views.delete_books, name='delete_book'),
    path('add_new_books_sections/',views.add_new_book_section,name='add-book-section'),
    path('add-Reviews/',views.add_reviews,name='add-reviews'),
    path('edit-Reviews/<int:id>',views.edit_reviews,name='edit-reviews'),
    path('delete-Reviews/<int:id>',views.delete_reviews,name='delete-reviews'),

]