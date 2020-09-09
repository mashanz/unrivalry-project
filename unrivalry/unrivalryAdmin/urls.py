# -*- encoding: utf-8 -*-
from django.urls import path
from .views import AdminViews

urlpatterns = [
    path('', AdminViews.index),
    path('video', AdminViews.video),
]
