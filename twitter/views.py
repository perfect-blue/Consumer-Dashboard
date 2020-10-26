from django.shortcuts import render
from twitter import forms
from .models import Twitter
# Create your views here.
def follower(request):
    twitter_form = forms.TwitterForm()
    twitter_dict = {'twitter_form':twitter_form}
    if request.method == 'POST':
        twitter_form = forms.TwitterForm(request.POST)

        if twitter_form.is_valid():
            consumer_key = twitter_form.cleaned_data['consumer_key']
            consumer_secret = twitter_form.cleaned_data['consumer_secret']
            access_token = twitter_form.cleaned_data['access_token']
            access_token_secret = twitter_form.cleaned_data['access_token_secret']
            username=twitter_form.cleaned_data['username']
            path=twitter_form.cleaned_data['path']

            auth=Twitter.auth(consumer_key,consumer_secret)
            auth.set_access_token(access_token,access_token_secret)

            api=Twitter.api(auth)

            follower_ids=Twitter.get_follower(username,api)
            following_ids=Twitter.get_following(username,api)

            follower_details=Twitter.get_username(follower_ids,api)
            following_details=Twitter.get_username(following_ids,api)


            twitter_dict['status']=Twitter.normalize_users(follower_details,following_details,username,path)
            return render(request,'Twitter/follower.html',twitter_dict)

    return render(request,'Twitter/follower.html',twitter_dict)
