from django import forms
from django.core import validators

class HistoricalForm(forms.Form):
    client = forms.CharField()
    access_key = forms.CharField()
    cities= forms.CharField()
    date = forms.CharField()
    hour = forms.CharField()

class TimeSeriesForm(forms.Form):
    client = forms.CharField()
    access_key = forms.CharField()
    cities = forms.CharField()
    historical_date_start = forms.CharField()
    historical_date_end = forms.CharField()
    hourly=forms.CharField(max_length=2)

class CurrentForm(forms.Form):
    client= forms.CharField()
    access_key = forms.CharField()
    city = forms.CharField()
