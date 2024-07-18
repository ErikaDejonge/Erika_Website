from django.shortcuts import render

# Create your views here.
def Admin(request):
    return render(request, 'main/admin.html')

def book_erika(request):
    return render ( request, 'pages/tables/book_erika.html')