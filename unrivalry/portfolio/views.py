# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django import template
from django.utils.safestring import mark_safe


class PortfolioViews():
    def index(request):
        return render(request, "portfolio/index.html", {})
