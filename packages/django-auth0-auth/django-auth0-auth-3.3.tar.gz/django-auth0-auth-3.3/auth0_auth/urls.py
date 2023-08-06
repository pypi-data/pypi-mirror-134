from .views import auth, callback, logout
from django.urls import re_path


urlpatterns = [
    re_path(r'^login/$', auth, name='auth0_login'),
    re_path(r'^logout/$', logout, name='auth0_logout'),
    re_path(r'^callback/$', callback, name='auth0_callback'),
]
