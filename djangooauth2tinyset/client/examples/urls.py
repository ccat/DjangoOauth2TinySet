
from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls.i18n import i18n_patterns

admin.autodiscover()

urlpatterns = [
    url(r'^accounts/', include('social.apps.django_app.urls', namespace='social')),#
]

urlpatterns += i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),
)
