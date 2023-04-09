from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


# Create your views here.

def home(request):
    weather = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=fce82447e26f829b9a3e17cd872aded6'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm
    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(weather.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
            'country': res['sys']['country'],
        }
        all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'form': form,
    }
    return render(request, 'main/homepage.html', context)
