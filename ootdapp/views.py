from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from ootdapp.models import Write
# API
from django.shortcuts import render
import requests
from time import sleep

url = "http://api.openweathermap.org/data/2.5/weather"



# Create your views here.
def main(request):
    ootdapps=Write.objects

    ### API
    prov_list = [
        {'name' : 'Seoul', 'city_id':'1835847'}
    ]

    def converte_kelvin_to_celsius(k):
        return (k-273.15)


    weather_info_list = []
    weather_info2_list = []
    for i in range(len(prov_list)):
        city_id = prov_list[i]['city_id']
        city_name = prov_list[i]['name']
        params = dict(
            id = city_id,
            APPID = '9b49c0e28142d30ad18ef5661507231e',
        )
        sleep(1)
        resp = requests.get(url=url, params=params)
        data = resp.json()
        if(data['cod'] == 429):
            break
        data_main = data['main']
        data_weather = data['weather']
        info = [
            
            city_name,\
            converte_kelvin_to_celsius(data_main['temp']), \
            data_main['humidity']

            
            
        ]
        
        weather_info = [
            data_weather[i]['main'],\
            data_weather[i]['description'],
            data_weather[i]['icon'],
        ]
        link = "http://openweathermap.org/img/wn/"+data_weather[i]['icon']+"@2x.png"
        description = data_weather[i]['description']
        tempcelcius=converte_kelvin_to_celsius(data_main['temp'])
        humidity = data_main['humidity']
        weather_info2_list.append(weather_info)
        weather_info_list.append(info)
        temp = weather_info_list[0]
        weather = weather_info2_list[0]
    return render(request, 'main.html', {'ootdapps':ootdapps, 'city_name':city_name, 'temp':temp, 'weather':weather, 'link':link,'c':tempcelcius,'humidity':humidity,'description':description})

def create(request):
    if request.method == 'POST':
        ootdapp=Write()
        ootdapp.title=request.POST['title']
        ootdapp.body=request.POST['body']
        ootdapp.image=request.FILES['image']
        ootdapp.pub_date=timezone.datetime.now()
        ootdapp.save()
        return redirect('main')
    else:
        return render(request, 'new.html')


def detail(request, pk):
    ootds = get_object_or_404(Write, pk=pk)
    return render(request, 'detail.html', {'ootds':ootds})


def home(request):

    prov_list = [
        {'name' : 'Seoul', 'city_id':'1835847'}
    ]

    def converte_kelvin_to_celsius(k):
        return (k-273.15)


    weather_info_list = []
    weather_info2_list = []
    for i in range(len(prov_list)):
        city_id = prov_list[i]['city_id']
        city_name = prov_list[i]['name']
        params = dict(
            id = city_id,
            APPID = '9b49c0e28142d30ad18ef5661507231e',
        )
        sleep(1)
        resp = requests.get(url=url, params=params)
        data = resp.json()
        if(data['cod'] == 429):
            break
        data_main = data['main']
        data_weather = data['weather']
        info = [
            
            city_name,\
            converte_kelvin_to_celsius(data_main['temp']), \
            
            
        ]
        
        weather_info = [
            data_weather[i]['main'],\
            data_weather[i]['icon'],
        ]
        link = "http://openweathermap.org/img/wn/"+data_weather[i]['icon']+"@2x.png"
        weather_info2_list.append(weather_info)
        weather_info_list.append(info)
        temp = weather_info_list[0]
        weather = weather_info2_list[0]
    return render(request, 'home.html', {'city_name':city_name, 'temp':temp, 'weather':weather, 'link':link})