from django.urls import path
from .import views

urlpatterns =[
    path('',views.admin_Login,name='admin-sign-in'),
    path('sign-out/',views.sign_out, name='sign-out'),
    path('mail-remove/<int:id>',views.Delete_element.mail_remove, name='mail_remove'),
    # Dashboard source code

    path('Dashboard/',views.dashboard, name='erika-dashboard'),
    path('Book/',views.book_erika, name='book-erika'),
    path('email/',views.email, name='email'),
    path('form/',views.form),
    path('blog/',views.blog, name='blog'),

]