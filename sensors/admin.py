from django.contrib import admin
from .models import Dht, Water, Bmp, Settings

admin.site.register(Dht)

admin.site.register(Bmp)


admin.site.register(Water)


class SettingsAdmin(admin.ModelAdmin):

    list_display = ('user_name',)
    list_display_links = ('user_name',)

admin.site.register(Settings, SettingsAdmin)