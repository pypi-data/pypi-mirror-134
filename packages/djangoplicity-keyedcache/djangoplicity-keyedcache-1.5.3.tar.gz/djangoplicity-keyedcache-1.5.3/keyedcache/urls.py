"""
URLConf for Caching app
"""

try:
	from django.conf.urls import url
except ImportError:
	from django.conf.urls.defaults import patterns

from keyedcache import views

urlpatterns = [
    url(r'^$', views.stats_page, name='keyedcache_stats'),
    url(r'^view/$', views.view_page, name='keyedcache_view'),
    url(r'^delete/$', views.delete_page, name='keyedcache_delete'),
]
