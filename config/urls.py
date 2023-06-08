from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from account.views import Login, Register, activate

from .sitemaps import StaticViewSitemap

sitemaps = {"static": StaticViewSitemap}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("cleanWorld.urls")),
    path("login/", Login.as_view(), name="login"),
    path("", include("django.contrib.auth.urls")),
    path("account/", include("account.urls"), name="account"),
    path("register/", Register.as_view(), name="register"),
    path("activate/<uidb64>/<token>/", activate, name="activate"),
    path("", include("social_django.urls", namespace="social")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "config.views.page_not_found_view"
handler500 = "config.views.handler500"
handler403 = "config.views.handler403"
