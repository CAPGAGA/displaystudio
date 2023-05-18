from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticSitemap(Sitemap):
    changefreq = "monthly"
    # priority = 1
    protocol = 'https'

    def items(self):
        return ['index', 'home-decor-gallery', 'kitchen-decor-gallery', 'shatters-gallery', 'form']

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        return {'index': 1.0, 'form': 1.0, 'home-decor-gallery': 0.9, 'kitchen-decor-gallery': 0.9, 'shatters-gallery': 0.9}[item]