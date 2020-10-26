from django.conf.urls import url,include
from twitter import views

app_name='twitter'

urlpatterns =[
    url(r'^follower/$',views.follower,name='follower'),
]
