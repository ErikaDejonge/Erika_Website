from django.urls import path
from .import views

urlpatterns =[
    path('',views.Admin, name='admin'),
    path('Book/',views.book_erika, name='book-erika'),

]