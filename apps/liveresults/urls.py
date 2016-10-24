from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'liveresults'

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="liveresults/index.html"),
        name='liveresults'),
]
