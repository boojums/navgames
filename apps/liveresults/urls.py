from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework import routers

from . import views

app_name = 'liveresults'

router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'races', views.RaceViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', TemplateView.as_view(template_name="liveresults/index.html"),
        name='liveresults'),
]
