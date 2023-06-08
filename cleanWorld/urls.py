from django.urls import path

from .views import home, robots

app_name = "cleanWorld"
urlpatterns = [
    path("", home, name="home"),
    path("robots.txt", robots, name="robots"),
]
