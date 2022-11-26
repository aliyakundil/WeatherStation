from django.urls import path
from .views import index, weather, metcast

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('weather/', weather, name='weather'),
    path('metcast/', metcast, name='metcast'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

