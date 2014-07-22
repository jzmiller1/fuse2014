from django.contrib.sitemaps import Sitemap


class MainSitemap(Sitemap):
    location = "/"
    changefreq = "monthly"
    priority = "1"

    def items(self):
        return [self]
