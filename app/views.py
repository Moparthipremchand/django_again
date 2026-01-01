from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# def Home(request):
#     return HttpResponse("this is http response home view")

def Home(request):
    return render(request, "Home.html")

def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")