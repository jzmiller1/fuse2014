from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.sitemaps import GenericSitemap
from django.http import HttpResponse
from fuse2014.sitemaps import MainSitemap
from cemeteries.models import Person, Cemetery

sitemaps = {
    'mainpage': MainSitemap,
    'people': GenericSitemap({'queryset': Person.objects.all(), }, changefreq='monthly', priority=0.6),
    'cemeteries': GenericSitemap({'queryset': Cemetery.objects.all(), }, changefreq='monthly', priority=0.6),
}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fuse2014.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cemeteries.urls', namespace='cemeteries')),
    url(r'^api/v1/', include('cemeteries.api_urls', namespace='cemeteries_api')),
    url(r'^search/', include('haystack.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^sitemap\.xml$',
        'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /api/", content_type="text/plain"))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

