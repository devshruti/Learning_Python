from django.shortcuts import render
from django.http import JsonResponse

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

def weather_view(request, city):
    city_data = weather_data.get(city)
    if city_data:
        return JsonResponse(city_data)
    else:
        return JsonResponse({'error': 'City not found'}, status=404)


