from django.conf.urls import patterns, include, url

from views import *

urlpatterns =[
    url(r"^basicinfo/$", APIbasicinfoView,name="profiles_api_basicinfo"),
]

"""
urlpatterns = patterns("",
    #url(r"^$", dashboardView,name="ciservices_dashboard"),
    url(r"^$", latestJVNview,name="securityalert_latest_jvn"),
    url(r"^dashboard/$", dashboardView,name="securityalert_dashboard"),
    url(r"^jvn/$", showJvnListView,name="securityalert_show_jvnlist"),
    url(r"^jvn/item/(?P<id>\d+)/$", showJvnView,name="securityalert_show_jvn"),
    url(r"^config/(?P<id>\d+)/$", configChangeView,name="securityalert_config_change"),
    url(r"^config/jvn/(?P<id>\d+)/$", configChangeByJVNidView,name="configChangeByJVNidView"),
    url(r"^config/$", configView,name="securityalert_config"),
)
"""
