from django.conf.urls import url
from . import views
                    
urlpatterns = [
        url(r'shows/new$', views.new_show),
        url(r'shows$', views.shows),
        url(r'create$', views.create),
        url(r'^shows/(?P<id>\d+)$', views.show_info),
        url(r'^shows/(?P<id>\d+)/edit$', views.edit_info),
        url(r'^shows/(?P<id>\d+)/update$', views.update_info),
        url(r'^shows/(?P<id>\d+)/destroy$', views.destroy),
]