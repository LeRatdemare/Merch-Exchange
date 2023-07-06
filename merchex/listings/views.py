from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', context={'bands': bands})


def band_detail(request, band_id):  # id est l'argument passé dans l'URL
    try:
        band = get_object_or_404(Band, id=band_id)
    except:
        return redirect('band-list')

    try:
        listings = get_list_or_404(Listing, band=band_id)
    except:
        listings = None
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

    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f"Message from {form.cleaned_data['name'] or 'anonyme'} via MerchEx Contact Us form",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['lufuluabon@outlook.fr']
            )
            return redirect('email-sent')
    else:
        # Cas où c'est la méthode GET
        form = ContactUsForm()
    return render(request, 'listings/contact.html', {'form': form})


def email_sent(request):
    return render(request, 'listings/email_sent.html')
