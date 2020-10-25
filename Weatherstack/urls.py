from django.conf.urls import url,include
from Weatherstack import views

app_name = 'Weatherstack'

urlpatterns =[
    url(r'^batch/$',views.batch,name='batch'),
    url(r'^time-series/$',views.time_series, name='time-series'),
    url(r'^ current/$',views.current,name='current'),
    url(r'^ stream/$',views.stream,name='stream')
]
