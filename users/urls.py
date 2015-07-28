from django.conf.urls import patterns, url, include

from rest_framework import routers

from .views import UserViewSet, CurrentUserView, TokenRefreshView, \
    TokenLoginView, SessionLoginView

user_router = routers.DefaultRouter()
user_router.register(r'users', UserViewSet)

urlpatterns = patterns(
    'api.users',
    url(r'users/me/$', CurrentUserView.as_view(), name='me'),
    url(r'users/refresh/$', TokenRefreshView.as_view(), name='refresh'),
    url(r'users/login/$', TokenLoginView.as_view(), name='login'),
    url(r'^', include(user_router.urls)),
)
