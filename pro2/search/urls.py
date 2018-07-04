from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from .views import (searchposts)
app_name = 'search'
urlpatterns = [
    url(r'^$', searchposts, name='searchposts'),

]
