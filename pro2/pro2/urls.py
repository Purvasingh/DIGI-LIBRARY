"""pro2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from app2.views import model_form_upload
from .views import login_page,home_page, logout_page,contact_page
from django.conf import settings
from django.conf.urls.static import static
from subjects.views import CseView, EceView, ITView

urlpatterns = [
    url(r'^$',home_page,name="home"),
    url(r'^upload/$',model_form_upload,name='upload'),
    url(r'^login/$',login_page,name="login"),
    url(r'^admin/', admin.site.urls),
    url(r'^search/', include('search.urls', namespace='search')),
    url(r'^logout/$',logout_page,name="logout"),
    url(r'^cse/$',CseView,name="cse"),
    url(r'^ece/$',EceView,name="ece"),
    url(r'^it/$',ITView,name="it"),
    url(r'^contact/$',contact_page,name="contact"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
