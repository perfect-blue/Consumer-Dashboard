from django.db import models
import tweepy
import pandas as pd

# Create your models here.
class Twitter():

    def auth(consumer_key,consumer_secret):
        return tweepy.OAuthHandler(consumer_key,consumer_secret)

    def api(auth):
        return tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

    def get_following(username,api):
        result=[]
        for user in tweepy.Cursor(api.friends_ids,screen_name=username,count=5000).items():
            result.append(user)
        return result

    def get_follower(username,api):
        result=[]
        for user in tweepy.Cursor(api.followers_ids, screen_name=username,count=5000).items():
            result.append(user)
        return result


    def get_username(userids,api):
        detail_dict={}
        fullusers=[]
        u_count=len(userids)
        try:
            for i in range(int(u_count/100)+1):
                end_loc = min((i+1)*100,u_count)
                fullusers.extend(
                    api.lookup_users(user_ids=userids[i*100:end_loc])
                )
            detail_dict['fullusers']=fullusers
            detail_dict['u_count']=u_count
            return detail_dict
        except:
            import traceback
            traceback.print_exc()
            return ['Something went wrong, quitting...']


    def normalize_users(follower,following,username,path):
        # try:
        follower_dicts=[]
        following_dicts=[]

        for x in follower['fullusers']:
            follower_dicts.append(x.__dict__)

        for x in following['fullusers']:
            following_dicts.append(x.__dict__)

        follower_csv=pd.json_normalize(follower_dicts)
        following_csv=pd.json_normalize(following_dicts)

        follower_csv = follower_csv[['id','id_str','name','screen_name','location','description',
                      'url','protected','followers_count','friends_count','listed_count',
                      'created_at','favourites_count','utc_offset','time_zone','geo_enabled',
                      'verified','statuses_count', 'lang','status','profile_image_url_https']]

        following_csv = following_csv[['id','id_str','name','screen_name','location','description',
                      'url','protected','followers_count','friends_count','listed_count',
                      'created_at','favourites_count','utc_offset','time_zone','geo_enabled',
                      'verified','statuses_count', 'lang','status','profile_image_url_https']]

        follower_csv.to_csv('{}\{}_follower.csv'.format(path,username,username))
        following_csv.to_csv('{}\{}_following.csv'.format(path,username,username))

        return '{} has {} followers and {} friends. Data has been saved to {}'.format(username,follower['u_count'],following['u_count'],path)
        # except:
        #     return "Limit have been reached wait for 15 minutes"
