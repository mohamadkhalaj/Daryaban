from django.contrib.auth import views
from django.urls import path

from .views import (
    CleanerProfile,
    Profile,
    Report,
    dashboard,
    dirtyAddress,
    dirtyPlaces,
    makeClean,
    removeReport,
    userProfile,
)

app_name = 'account'

urlpatterns = [
    path('dashboard/<int:page>', dashboard, name='dashboard'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', Profile.as_view(), name='profile'),
    path('dirtyPlaces/<int:page>', dirtyPlaces, name='dirtyPlaces'),
    path('dirtyPlaces/', dirtyPlaces, name='dirtyPlaces'),
    path('makeClean/<int:pk>', makeClean, name='makeClean'),
    path('userProfile/<int:pk>', userProfile, name='userProfile'),
    path('CleanerProfile/<int:pk>', CleanerProfile, name='CleanerProfile'),
    path('dirtyAddress/<coordinates>', dirtyAddress, name='dirtyAddress'),
    path('report/', Report.as_view(), name='report'),
    path('removeReport/<int:pk>', removeReport, name='removeReport'),
]
