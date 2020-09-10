# -*- encoding: utf-8 -*-
from django.urls import path, re_path
from . import views as web
from .views import WebViews

urlpatterns = [
    path('', WebViews.index, name="home"),
    # Matches any html file
    re_path(r'^.*\.*', WebViews.pages),
]
