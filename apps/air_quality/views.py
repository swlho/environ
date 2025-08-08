from django.shortcuts import render
import requests, os
import geocoder
from apps.air_quality.utils.get_aq_rating import get_aq_rating


# Create your views here.
def index(request):
    key = os.getenv("AQ_USERNAME_KEY")
    api_key = os.getenv("WEATHER_API_KEY")
    city = request.GET.get('city')
    location = geocoder.geonames(city, key=key).latlng
    lat = location[0]
    lon = location[1]
    url = "http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
    api_request = url.format(lat=lat, lon=lon, api_key=api_key)
    aq_data = requests.get(api_request).json()
    aq_rating = get_aq_rating(aq_data["list"][0]["main"]["aqi"])
    context = {'aq_data': aq_data, 'aq_rating': aq_rating}
    return render(request, 'apps/air_quality.html', context)
