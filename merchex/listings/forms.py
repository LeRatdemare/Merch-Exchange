from django import forms
from listings.models import Band, Listing


class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)


class BandForm(forms.ModelForm):

    class Meta:
        model = Band
        exclude = ('active', 'official_homepage')
        # fields = '__all__' # Pour que tous les champs du modèle soient ajoutés au formulaire


class ListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        exclude = ('sold',)
        # fields = '__all__'
