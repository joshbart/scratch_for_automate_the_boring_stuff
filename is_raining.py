#!/usr/bin/env python

import time
# import requests
# import json

# weather_api = requests.get(https://api.weather.gov/stations/KFAR/observations/latest)

def get_weather():
    # Need to implement code that looks up the properties.precipitationLastHour.value property from the weather_api
    return True

def read_parameters():
    # Need to implement code to read a parameter from the command line.
    return True

if __name__ == '__main__':
    is_raining = get_weather()
    have_umbrella = read_parameters()
    if is_raining == True:
        if have_umbrella == False:
            while is_raining == True:
                time.sleep(300)
                is_raining = get_weather()

print("Go outside!")