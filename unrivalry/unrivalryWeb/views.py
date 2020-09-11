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
        return render(request, "web/index.html")

    def google_seo(request):
        return render(request, "web/google0e8c41b27141026f.html")

    def pages(request):
        context = {}
        # All resource paths end in .html.
        # Pick out the html file name from the url. And load that template.
        try:
            load_template = request.path.split('web/')[-1]
            html_template = loader.get_template(load_template)
            return HttpResponse(html_template.render(context, request))

        except template.TemplateDoesNotExist:
            html_template = loader.get_template('web/page-404.html')
            return HttpResponse(html_template.render(context, request))

        except:
            html_template = loader.get_template('web/page-500.html')
            return HttpResponse(html_template.render(context, request))
