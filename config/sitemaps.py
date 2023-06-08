from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewSitemap(Sitemap):
    def items(self):
        return [
            "login",
            "register",
            "cleanWorld:home",
            "account:dashboard",
            "account:profile",
            "account:dirtyPlaces",
            "account:report",
        ]

    def location(self, item):
        return reverse(item)
