from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home_view(request):
    return render(request, template_name="pages/home.html")

def contact_view(request):
    return render(request, template_name="pages/contact.html")