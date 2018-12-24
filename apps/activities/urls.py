''' Urls for the Activities app. '''
from django.conf.urls import url

from . import views

app_name = 'activities'

urlpatterns = [
    url(r'^$', views.ActivityList.as_view(), name='activity-list'),
    url(r'detail/(?P<slug>[\w\-]+)/$', views.ActivityDetail.as_view(),
        name='activity-detail'),
    #url(r'add/$', views.EventCreate.as_view(), name='event-add'),
    #url(r'delete/(?P<slug>[\w\-]+)/$', views.EventDelete.as_view(),
    #    name='event-delete'),
]
