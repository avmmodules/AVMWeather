'''
    Description: Get weather data in a simple way.
    Author: aulerjbailey
    Version: 1.0.0
    Video: https://youtu.be/UAVD6qK38kQ
'''
import requests as req

def get_weather(lat, lon, api_key):
    ''' All process of getting information '''
    api_url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}'
    try:
        # request to api
        response = req.get(api_url)
        return response.json()
    except req.exceptions.RequestException as e:
        print(e)