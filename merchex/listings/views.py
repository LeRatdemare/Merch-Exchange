from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm, BandForm, ListingForm
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


def band_create(request):

    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            # Version longue :
            # band = Band()
            # band.name = form.cleaned_data['name']
            # band.genre = form.cleaned_data['genre']
            # band.biography = form.cleaned_data['biography']
            # band.year_formed = form.cleaned_data['year_formed']
            # band.active = form.cleaned_data['active']
            # band.official_homepage = form.cleaned_data['official_homepage']
            # band.save()
            return redirect('band-detail', band.id)
    else:
        # Cas où c'est la méthode GET
        form = BandForm()
    return render(request, 'listings/band_create.html', {'form': form})


def band_update(request, band_id):
    band = get_object_or_404(Band, id=band_id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            print("Yessssssssss")
            return redirect('band-detail', band.id)
    else:
        print("Noooooo")
        form = BandForm(instance=band)  # On pré-rempli le formulaire
    return render(request, 'listings/band_update.html', {'form': form, 'band': band})


def about(request):
    author = "Nathan Lufuluabo"
    return render(request, 'listings/about.html', context={'author': author})


def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', context={'listings': listings})


def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    return render(request, 'listings/listing_detail.html', {'listing': listing})


def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm()
    return render(request, 'listings/listing_create.html', {'form': form})


def listing_update(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm(instance=listing)
    return render(request, 'listings/listing_update.html', {'form': form, 'listing': listing})


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
