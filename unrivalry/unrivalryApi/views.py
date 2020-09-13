# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django import template
from django.utils.safestring import mark_safe
from django.core import serializers
from django.http.response import JsonResponse
import datetime
import json
import ast
from unrivalryWeb import models as modelWeb
from allauth.socialaccount import models as modelAllauth
from django.contrib.auth.models import User


class ApiViews():
    def index(request):
        return render(request, "api/index.html")

    def test(request):
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

    def test_model(request):
        some_queryset = User.objects.all()
        serialized_queryset = serializers.serialize('python', some_queryset)
        return JsonResponse(serialized_queryset, safe=False)

    def social_user(request):
        some_queryset = modelAllauth.SocialAccount.objects.all()
        x = {}
        new_model = []
        for i in some_queryset:
            x = ast.literal_eval(str(i.extra_data))
            x["id"] = i.user.id
            new_model.append(x)
        serialized_queryset = serializers.serialize('python', some_queryset)
        return JsonResponse(new_model, safe=False)
