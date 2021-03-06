# -*- encoding: utf-8 -*-
from django.urls import path, re_path
from . import views as web
from .views import DSViews

urlpatterns = [
    path('', DSViews.index),
    # Matches any html file
    re_path(r'^.*\.*', DSViews.pages),
]
