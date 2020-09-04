# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django import template
from django.utils.safestring import mark_safe
import datetime


class WebViews():
    def index(request):
        # return HttpResponse("Web Index")
        return render(request, "web/index.html")

    def test(request):
        print("OH")
        x = [1, 4, 2, 5, 7, 8, 6, 3, 8, 7, 9, 8, 0]
        k = 0
        for i in x:
            k += i
        response = JsonResponse(
            {
                'foo': 'bar',
                'x': x,
                'k': k
            }
        )
        return response
