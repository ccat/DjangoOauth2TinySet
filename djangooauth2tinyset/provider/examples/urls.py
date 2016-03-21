
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

admin.autodiscover()

urlpatterns = [
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/', include("djangooauth2tinyset.provider.urls_api")),
]

urlpatterns += i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),
)
