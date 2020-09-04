# -*- encoding: utf-8 -*-
from django.urls import path
from .views import PortfolioViews

urlpatterns = [
    path('', PortfolioViews.index),
]
