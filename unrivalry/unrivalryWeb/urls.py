# -*- encoding: utf-8 -*-
from django.urls import path
from . import views as web
from .views import WebViews

urlpatterns = [
    path('', WebViews.index),
    path('web_test', WebViews.test, name="web_test")
]
