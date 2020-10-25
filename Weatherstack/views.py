from django.shortcuts import render
from Weatherstack import forms
from .models import Batch
from .models import Stream
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
    time_series_form=forms.TimeSeriesForm()
    time_series_dict = {'time_series_form':time_series_form}
    if request.method == 'POST':
        time_series_form = forms.TimeSeriesForm(request.POST)

        if time_series_form.is_valid():
           client = time_series_form.cleaned_data['client']
           access_key = time_series_form.cleaned_data['access_key']
           cities = time_series_form.cleaned_data['cities']
           historical_date_start = time_series_form.cleaned_data['historical_date_start']
           historical_date_end = time_series_form.cleaned_data['historical_date_end']
           hourly=time_series_form.cleaned_data['hourly']
           time_series_dict['status']=Batch.get_time_series(client,access_key,cities,historical_date_start,
                                      historical_date_end,hourly)

           return render(request,'BatchWeather/timeseries.html',time_series_dict)

    return render(request,'BatchWeather/timeseries.html',time_series_dict)

def current(request):
    current_form=forms.CurrentForm()
    current_dict = {'current_form':current_form}

    if request.method =='POST':
        current_form = forms.CurrentForm(request.POST)

        if current_form.is_valid():
            client = current_form.cleaned_data['client']
            access_key = current_form.cleaned_data['access_key']
            city = current_form.cleaned_data['city']

            current_dict['status']=Batch.get_current(client,access_key,city)

            return render(request,'BatchWeather/current.html',current_dict)

    return render(request,'BatchWeather/current.html',current_dict)

def stream(request):
    stream_form=forms.StreamForm()
    stream_dict = {'stream_form':stream_form}

    if request.method =='POST':
        stream_form = forms.StreamForm(request.POST)

        if stream_form.is_valid():
           client = stream_form.cleaned_data['client']
           access_key = stream_form.cleaned_data['access_key']
           city = stream_form.cleaned_data['city']

           return render(request,'StreamWeather/consumer.html',stream_dict)

    return  render(request,'StreamWeather/producer.html',stream_dict)
