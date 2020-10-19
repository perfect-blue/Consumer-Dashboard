from django.db import models
import requests
import json
# Create your models here.
class Batch():
    def get_historical(client,access_key,cities,date,hour):
        query={'access_key':access_key,'query':cities,
                'historical_date':date,'hourly':hour}

        response = requests.get("http://api.weatherstack.com/historical?",params=query)

        filepath='{}/{}.json'.format(client,'data')
        with open(filepath,'w') as fp:
            json.dump(response.json(),fp)

        return 'Historical weather data from {} has been added to {}'.format(cities,client)
