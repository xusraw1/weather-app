from django.shortcuts import render
import requests


# Create your views here.

def home(request):
    weather = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=fce82447e26f829b9a3e17cd872aded6'
    city = 'Tashkent'
    res = requests.get(weather.format(city)).json()
    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon'],
        'country': res['sys']['country'],
    }

    context = {
        'info': city_info,
    }
    return render(request, 'main/homepage.html', context)
