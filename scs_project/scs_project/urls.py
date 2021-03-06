from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    # Examples:
    # url(r'^$', 'scs_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('fmecango.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]
