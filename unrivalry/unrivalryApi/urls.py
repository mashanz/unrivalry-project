# -*- encoding: utf-8 -*-
from django.urls import path
from .views import ApiViews

urlpatterns = [
    path('', ApiViews.index),
    path('test', ApiViews.test),
]
