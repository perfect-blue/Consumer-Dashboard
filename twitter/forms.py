from django import forms
from django.core import validators

class TwitterForm(forms.Form):
    consumer_key = forms.CharField()
    consumer_secret = forms.CharField()
    access_token = forms.CharField()
    access_token_secret = forms.CharField()
    username=forms.CharField()
    path=forms.CharField()
