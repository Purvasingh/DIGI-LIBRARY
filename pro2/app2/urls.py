from django.conf.urls import url
from app2 import views

urlpatterns = [
    url(r'^$',views.help,name='help'),
    url(r'^$',views.gold,name='gold'),
    url(r'app2/^$',views.help,name='help'),
    url(r'app2/^$',views.gold,name='gold'),
]
