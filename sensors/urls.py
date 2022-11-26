from django.urls import path
from .views import sensors, graph

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', sensors, name='sensors'),
    path('graph/', graph, name='graph'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

