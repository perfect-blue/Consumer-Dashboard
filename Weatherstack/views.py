from django.shortcuts import render
from Weatherstack import forms
from .models import Batch
# Create your views here.
def index(request):
    return render(request,'index.html')

def batch(request):
    batchForm = forms.HistoricalForm()
    batch_dict = {'batchform':batchForm}
    if request.method == 'POST':
        batchForm = forms.HistoricalForm(request.POST)

        if batchForm.is_valid():
            print("Validation Success")
            client = batchForm.cleaned_data['client']
            access_key = batchForm.cleaned_data['access_key']
            cities = batchForm.cleaned_data['cities']
            date = batchForm.cleaned_data['date']
            hour = batchForm.cleaned_data['hour']
            batch_dict['status']=Batch.get_historical(client,access_key,cities,date,hour)
            return render(request,'BatchWeather/batch.html',batch_dict)

    return render(request,'BatchWeather/batch.html',batch_dict)

def time_series(request):
    return render(request,'BatchWeather/timeseries.html')
