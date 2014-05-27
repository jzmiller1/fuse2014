from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fuse2014.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cemeteries.urls', namespace='cemeteries')),
    url(r'^search/', include('haystack.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

