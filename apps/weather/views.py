from django.shortcuts import get_object_or_404, redirect, render
import requests, os

from apps.weather.utils.get_celsius_temp import get_celsius_temp
from .models import City
from .forms import CityForm


def index(request):
    api_key = os.getenv("WEATHER_API_KEY")
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'

    cities = City.objects.all() #return all the cities in the database

    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = CityForm()

    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city, api_key)).json() #request the API data and convert the JSON to Python data types

        celsius_temp = get_celsius_temp(city_weather['main']['temp'])

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'celsius' : celsius_temp,
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) #add the data for the current city into our list

    context = {'weather_data' : weather_data, 'form' : form}

    return render(request, 'apps/weather.html', context) #returns the index.html template

def city_delete(request, pk):
    city = get_object_or_404(City, pk=pk)

    if request.method == 'POST':
        city.delete()
        return redirect('/weather')
