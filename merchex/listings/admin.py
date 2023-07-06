from django.contrib import admin
from listings.models import Band, Listing


class BandAdmin(admin.ModelAdmin):
    # La liste des champs à afficher dans l'admin
    list_display = ('name', 'year_formed', 'genre')


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'sold', 'year', 'type', 'band')


# Register your models here.
admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
