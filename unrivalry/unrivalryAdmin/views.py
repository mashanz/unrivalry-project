# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django import template
from django.utils.safestring import mark_safe
import datetime


class AdminViews():
    @login_required(login_url="/login/")
    def index(request):
        # return HttpResponse("Admin Index")
        return render(request, "adm/index.html")
