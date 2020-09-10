# -*- encoding: utf-8 -*-
from django.urls import path
from .views import AdminViews

urlpatterns = [
    # path('', AdminViews.index),
    path('', AdminViews.dashboard),
    path('profile', AdminViews.profile),
    path('server_profiling', AdminViews.server_profiling),
    path('album', AdminViews.album),
    path('music', AdminViews.music),
    path('video', AdminViews.video),
    path('settings', AdminViews.settings),
]
