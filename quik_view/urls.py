"""quik_view URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from quik_view_app.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^load_data/?$', add_static_data),
    url(r'^get_geo/?', get_all_geo),
    url(r'^/?$', home),
    url(r'^map/?$', map_plot),
    url(r'^trending/?$', trending_plot),
    url(r'^live_stat/?$', live_data_render),
    url(r'^get_live/?$', get_live_data),
    url(r'^get_trending/?$', get_trending_data),
    url(r'^get_heat_map/?$', get_heat_map),
    url(r'^get_loc_ad/?$', get_ads_by_location),
    url(r'^get_heat_map_city_data/?$', get_ad_internal)
]
