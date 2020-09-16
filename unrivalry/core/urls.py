# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    # Custom App URL
    path("dashboard", include("unrivalryAdmin.urls")),
    path("dashboard/", include("unrivalryAdmin.urls")),
    path("api", include("unrivalryApi.urls")),
    path("api/", include("unrivalryApi.urls")),
    path("portfolio", include("portfolio.urls")),
    path("portfolio/", include("portfolio.urls")),

    # Core App URL
    path('users/', include('django.contrib.auth.urls')),
    path('soclog/', TemplateView.as_view(template_name="soclog/index.html")),
    path('devadmin', admin.site.urls),          # Django admin route
    path('devadmin/', admin.site.urls),         # Django admin route
    path('accounts/', include('allauth.urls')),
    # Auth routes - login / register
    path("", include("authentication.urls")),

    # Everything Else under this is unknown or 404
    path("templates", include("app.urls")),     # UI Kits Html files
    path("templates/", include("app.urls")),    # UI Kits Html files
    path("", include("unrivalryWeb.urls")),
]
