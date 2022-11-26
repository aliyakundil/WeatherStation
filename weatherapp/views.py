import requests
from django.shortcuts import render
from .models import City, Metcast
from .forms import CityForm, MetcastForm

def index(request):

    #погода
    appid = 'd7c1f542dcb8ce32cdfdccd7819cbd21'

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'pressure': res['main']['pressure'],
            'humidity': res['main']['humidity'],
            'icon': res['weather'][0]['icon']  # список
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities}

    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    #return render(request, 'default.html',
     #                 {'mapbox_access_token': mapbox_access_token})
    return render(request, 'weather/index.html', {'mapbox_access_token': mapbox_access_token, 'all_info': all_cities})

from datetime import datetime
from datetime import date
from datetime import time
from datetime import date
def weather(request):

    # погода
    appid = 'd7c1f542dcb8ce32cdfdccd7819cbd21'

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        #form.save()  # сохраняет данные в бд

    form = CityForm()  # очищает

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
                'city': city.name,
                'temp': res['main']['temp'],
                'pressure': res['main']['pressure'],
                'humidity': res['main']['humidity'],
                'description': res['weather'][0]['description'],
                'icon': res['weather'][0]['icon']  # список
        }

        all_cities.append(city_info)

    today = date.today()
    print(today)

    context = {'all_info': all_cities, 'form':form}

    return render(request, 'weather/weather.html', context)

def metcast (request):
    appid = 'd7c1f542dcb8ce32cdfdccd7819cbd21'

    url = 'https://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid=' + appid

    if (request.method == 'POST'):
        form = MetcastForm(request.POST)
        form.save() #сохраняет данные в бд

    form = MetcastForm() #очищает

    metcast = Metcast.objects.all()

    all_metcast = []
    all_prognozy2 = []

    for city in metcast:
        res = requests.get(url.format(city.name)).json()
        prognoz_info = {
            'city': city.name,
            'date': res['list'][0]['dt_txt'],
            'temp': res['list'][0]['main']['temp'],
            'temp_max': res['list'][0]['main']['temp_max'],
            'temp_min': res['list'][0]['main']['temp_min'],
            'pressure': res['list'][0]['main']['pressure'],
            'humidity': res['list'][0]['main']['humidity'],
            'icon': res['list'][0]['weather'][0]['icon'],  # список

            'city_night': city.name,
            'date_night': res['list'][5]['dt_txt'],
            'temp_night': res['list'][5]['main']['temp'],
            'temp_max_night': res['list'][5]['main']['temp_max'],
            'temp_min_night': res['list'][5]['main']['temp_min'],
            'pressure_night': res['list'][5]['main']['pressure'],
            'humidity_night': res['list'][5]['main']['humidity'],
            'icon_night': res['list'][5]['weather'][0]['icon'],  # список

            'city_2': city.name,
            'date_2': res['list'][8]['dt_txt'],
            'temp_2': res['list'][8]['main']['temp'],
            'temp_max_2': res['list'][8]['main']['temp_max'],
            'temp_min_2': res['list'][8]['main']['temp_min'],
            'pressure_2': res['list'][8]['main']['pressure'],
            'humidity_2': res['list'][8]['main']['humidity'],
            'icon_2': res['list'][8]['weather'][0]['icon'],  # список

            'city_night2': city.name,
            'date_night2': res['list'][13]['dt_txt'],
            'temp_night2': res['list'][13]['main']['temp'],
            'temp_max_night2': res['list'][13]['main']['temp_max'],
            'temp_min_night2': res['list'][13]['main']['temp_min'],
            'pressure_night2': res['list'][13]['main']['pressure'],
            'humidity_night2': res['list'][13]['main']['humidity'],
            'icon_night2': res['list'][13]['weather'][0]['icon'],  # список

            'city_3': city.name,
            'date_3': res['list'][16]['dt_txt'],
            'temp_3': res['list'][16]['main']['temp'],
            'temp_max_3': res['list'][16]['main']['temp_max'],
            'temp_min_3': res['list'][16]['main']['temp_min'],
            'pressure_3': res['list'][16]['main']['pressure'],
            'humidity_3': res['list'][16]['main']['humidity'],
            'icon_3': res['list'][16]['weather'][0]['icon'],  # список

            'city_night3': city.name,
            'date_night3': res['list'][21]['dt_txt'],
            'temp_night3': res['list'][21]['main']['temp'],
            'temp_max_night3': res['list'][21]['main']['temp_max'],
            'temp_min_night3': res['list'][21]['main']['temp_min'],
            'pressure_night3': res['list'][21]['main']['pressure'],
            'humidity_night3': res['list'][21]['main']['humidity'],
            'icon_night3': res['list'][21]['weather'][0]['icon'],  # список

            'city_4': city.name,
            'date_4': res['list'][24]['dt_txt'],
            'temp_4': res['list'][24]['main']['temp'],
            'temp_max_4': res['list'][24]['main']['temp_max'],
            'temp_min_4': res['list'][24]['main']['temp_min'],
            'pressure_4': res['list'][24]['main']['pressure'],
            'humidity_4': res['list'][24]['main']['humidity'],
            'icon_4': res['list'][24]['weather'][0]['icon'],  # список

            'city_night4': city.name,
            'date_night4': res['list'][30]['dt_txt'],
            'temp_night4': res['list'][30]['main']['temp'],
            'temp_max_night4': res['list'][30]['main']['temp_max'],
            'temp_min_night4': res['list'][30]['main']['temp_min'],
            'pressure_night4': res['list'][30]['main']['pressure'],
            'humidity_night4': res['list'][30]['main']['humidity'],
            'icon_night4': res['list'][30]['weather'][0]['icon'],  # список

            'city_5': city.name,
            'date_5': res['list'][34]['dt_txt'],
            'temp_5': res['list'][34]['main']['temp'],
            'temp_max_5': res['list'][34]['main']['temp_max'],
            'temp_min_5': res['list'][34]['main']['temp_min'],
            'pressure_5': res['list'][34]['main']['pressure'],
            'humidity_5': res['list'][34]['main']['humidity'],
            'icon_5': res['list'][34]['weather'][0]['icon'],  # список

            'city_night5': city.name,
            'date_night5': res['list'][39]['dt_txt'],
            'temp_night5': res['list'][39]['main']['temp'],
            'temp_max_night5': res['list'][39]['main']['temp_max'],
            'temp_min_night5': res['list'][39]['main']['temp_min'],
            'pressure_night5': res['list'][39]['main']['pressure'],
            'humidity_night5': res['list'][39]['main']['humidity'],
            'icon_night5': res['list'][39]['weather'][0]['icon'],  # список
        }

        all_metcast.append(prognoz_info)

    context = {'all_metcast': all_metcast}

    return render(request, 'weather/metcast.html', context)
