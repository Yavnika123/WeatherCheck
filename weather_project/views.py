# weather_app/views.py

from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from weather_app.models import City

def get_weather_data(request, city_id):
    try:
        # Get the city object corresponding to the given city_id
        city = get_object_or_404(City, id=city_id)

        # Make an API call to fetch weather data for the city
        api_key = '59df23788166a01b65d4c6226fb04c98'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city.name}&appid={api_key}&units=metric'

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            # Extract relevant weather information from the API response
            temperature = data['main']['temp']
            description = data['weather'][0]['description']

            # Create a dictionary with the weather data
            weather_data = {
                #'city': city.name,
                'temperature': f'{temperature}°C',
                'description': description
            }

            # Return weather data as JSON response
            return JsonResponse(weather_data)
        else:
            # Handle API error responses
            error_message = data.get('message', 'Unknown error')
            return JsonResponse({'error': error_message}, status=response.status_code)
    except City.DoesNotExist:
        # Handle the case where the requested city_id does not exist
        return JsonResponse({'error': 'City not found'}, status=404)



def index(request):
    # Your logic for the index view
    return render(request, 'index.html')

def about(request):
    # Your logic for the about view
    return render(request, 'about.html')

def weather(request):
    # Your logic for the weather view
    return render(request, 'weather.html')

def contact(request):
    # Your logic for the contact view
    return render(request, 'contact.html')
