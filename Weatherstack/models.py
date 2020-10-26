from django.db import models
import requests
import json
import pandas as pd
from time import sleep

class Batch():

    def get_current(client, access_key, city):
        query = {'access_key':access_key,'query':city}
        response = requests.get("http://api.weatherstack.com/current?",params=query)
        if(response.status_code==200):
            current_file = response.json()
            try:
                response = requests.get("http://api.weatherstack.com/current?",params=query)

                current=current_file['current']
                location=current_file['location']
                current['location']=location

                current_list=[]
                current_list.append(current)
                result = pd.json_normalize(current_list)
                return 'Current weather data from {} has been added to {}'.format(city,client)
            except:
                return current_file['error']['info']
        else:
            return '{}. Connection Error'.format(response.status_code)

    def get_historical(client,access_key,cities,date,hourly):
        query={'access_key':access_key,'query':cities,
                'historical_date':date,'hourly':hourly}

        response = requests.get("http://api.weatherstack.com/historical?",params=query)
        if(response.status_code==200):
            json_file=response.json()
            try:
                daily_list=[]
                historical = json_file['historical']
                location = json_file['location']
                for x in historical:
                    historical[x]['location']=location
                    daily_list.append(historical[x])

                result=pd.json_normalize(daily_list,'hourly',
                ['date','date_epoch','mintemp','maxtemp','avgtemp','totalsnow','sunhour','astro','location'])

                result.to_csv('{}'.format(client),index=False)
                return 'Daily weather data from {} has been added to {}'.format(cities,client)

            except:
                return json_file['error']['info']
        else:
            return 'Error. Check Again Your Input'

    def get_time_series(client,access_key,cities,historical_date_start,historical_date_end,hourly):
        query={'access_key':access_key,'query':cities,
                'historical_date_start':historical_date_start,
                'historical_date_end':historical_date_end,
                'hourly':hourly}

        response = requests.get("http://api.weatherstack.com/historical?",params=query)

        if(response.status_code==200):
            json_file = response.json()
            try:
                ts_list = []
                historical = json_file['historical']
                location = json_file['location']
                for x in historical:
                    historical[x]['location']=location
                    ts_list.append(historical[x])

                result=pd.json_normalize(ts_list,'hourly',
                ['date','date_epoch','mintemp','maxtemp','avgtemp','totalsnow','sunhour','astro','location'])

                result.to_csv('{}'.format(client),index=False)
                return 'Time-series weather data from {} has been added to {}'.format(cities,client)
            except:
                return json_file['error']['info']
        elif(response.status_code==400):
            return 'Error. Check Again Your Input'
        elif(response.status_code==500):
            return 'Server Error. Please check again Latter'

class Stream():
    def get_stream_data(client,access_key,city,status):
        while status==True:
            print("this is weather data")
            sleep(2)
        # return 'Stream weather data from {} has been added to {}'.format(city,client)'
