from django.shortcuts import render
from .models import City
import requests
from .forms import CityForm
# Create your views here.
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=32b66fcccb72a0ec9c7bea43576cbbd3'
    if request.method == 'POST':
        forms = CityForm(request.POST)
        forms.save()

    froms = CityForm()
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        r = requests.get(url.format(city)).json()
        #print(r.text)
        city_weather = {
            'city':city.name,
            'temperature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    print(city_weather)
    context = { 
        'weather_data' : weather_data,
        'form' : froms,
                }
    return render(request, 'weather/index.html', context)