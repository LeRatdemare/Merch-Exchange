from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from listings.models import Band
from listings.models import Listing


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', context={'bands': bands})


def band_detail(request, band_id):  # id est l'argument passé dans l'URL
    try:
        band = get_object_or_404(Band, id=band_id)
    except:
        return redirect('band-list')

    listings = get_list_or_404(Listing, band=band_id)
    return render(request, 'listings/band_detail.html', {'band': band, 'listings': listings})


def about(request):
    author = "Nathan Lufuluabo"
    return render(request, 'listings/about.html', context={'author': author})


def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', context={'listings': listings})


def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    return render(request, 'listings/listing_detail.html', {'listing': listing})


def contact(request):
    mail_pro = "nathan.lufuluabo@ensc.fr"
    return render(request, 'listings/contact.html', context={'mail_pro': mail_pro})
