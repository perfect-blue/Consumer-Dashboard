from django.db import models
import requests
import json
import pandas as pd

class Batch():

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
