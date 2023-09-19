from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band


def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})


def about(request):
    return HttpResponse('<h1>About Us</h1> <p>We love merch!</p>')


def contact(request):
    return HttpResponse('<h1>Contact Us</h1> <p>nadir.larhdir@gmail.com</p>')
