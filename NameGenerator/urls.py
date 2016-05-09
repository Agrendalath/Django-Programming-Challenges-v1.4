from django.conf.urls import url

from . import views
from .apps import NamegeneratorConfig

app_name = NamegeneratorConfig.name
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^names/(?P<sex>[m,f])/(?P<country>[0-9]+)$', views.display, name='names')
]
