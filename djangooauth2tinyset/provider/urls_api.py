from django.conf.urls import patterns, include, url

from views import *

urlpatterns =[
    url(r"^basicinfo/$", APIbasicinfoView,name="profiles_api_basicinfo"),
]
