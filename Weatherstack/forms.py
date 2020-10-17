from django import forms
from django.core import validators

class HistoricalForm(forms.Form):
    client = forms.CharField()
    access_key = forms.CharField()
    cities= forms.CharField()
    date = forms.CharField()
    hour = forms.CharField()
