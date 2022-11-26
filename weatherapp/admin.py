from django.contrib import admin
from .models import City, Metcast

class CityAdmin(admin.ModelAdmin):

    list_display = ('name',)
    list_display_links = ('name',)

admin.site.register(City, CityAdmin)

class MetcastAdmin(admin.ModelAdmin):

    list_display = ('name',)
    list_display_links = ('name',)

admin.site.register(Metcast, MetcastAdmin)