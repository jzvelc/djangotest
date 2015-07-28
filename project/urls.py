from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from .views import api

urlpatterns = patterns(
    '',
    url(r'^api/$', api),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('users.urls', namespace='api.users')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
