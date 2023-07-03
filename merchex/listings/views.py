from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing


def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', context={'bands': bands})


def about(request):
    author = "Nathan Lufuluabo"
    return render(request, 'listings/about.html', context={'author': author})


def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', context={'listings': listings})


def contact(request):
    mail_pro = "nathan.lufuluabo@ensc.fr"
    return render(request, 'listings/contact.html', context={'mail_pro': mail_pro})
