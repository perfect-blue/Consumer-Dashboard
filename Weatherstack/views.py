from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def batch(request):
    return render(request,'BatchWeather/batch.html')

def time_series(request):
    return render(request,'BatchWeather/timeseries.html')        
