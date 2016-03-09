from django.conf.urls import include, url
from fmecango import views

urlpatterns = [

    url(r'^$', 'fmecango.views.index', name='index'),
    url(r'^(?P<slug>[\w-]+)/$', 'views.table', name='index'),
]
