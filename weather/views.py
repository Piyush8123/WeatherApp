import json

from django.shortcuts import render
import requests


def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=58216e3c59b90e3957a62dc89f70fd83'
        data = requests.get(url)
        data = data.json()

        return render(request,'weather/index.html',{'response':data})

    return render(request,'weather/index.html')
