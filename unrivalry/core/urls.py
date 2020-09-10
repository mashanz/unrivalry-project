# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    # Custom App URL
    path("dashboard", include("unrivalryAdmin.urls")),
    path("dashboard/", include("unrivalryAdmin.urls")),
    path("api", include("unrivalryApi.urls")),
    path("api/", include("unrivalryApi.urls")),
    path("portfolio", include("portfolio.urls")),
    path("portfolio/", include("portfolio.urls")),

    # Core App URL
    path('soclog/', TemplateView.as_view(template_name="soclog/index.html")),
    path('devadmin', admin.site.urls),            # Django admin route
    path('devadmin/', admin.site.urls),           # Django admin route
    path('accounts/', include('allauth.urls')),
    path("", include("authentication.urls")),  # Auth routes - login / register
    path("", include("unrivalryWeb.urls")),
    # path("", include("app.urls")),             # UI Kits Html files
]
