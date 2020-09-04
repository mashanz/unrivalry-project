# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    # Custom App URL
    path("", include("unrivalryWeb.urls")),
    path("adm", include("unrivalryAdmin.urls")),
    path("adm/", include("unrivalryAdmin.urls")),
    path("api", include("unrivalryApi.urls")),
    path("api/", include("unrivalryApi.urls")),
    path("portfolio", include("portfolio.urls")),
    path("portfolio/", include("portfolio.urls")),

    # Core App URL
    # path('admin', admin.site.urls),            # Django admin route
    # path('admin/', admin.site.urls),           # Django admin route
    path("", include("authentication.urls")),  # Auth routes - login / register
    path("", include("app.urls")),             # UI Kits Html files
]
