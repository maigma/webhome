from django.shortcuts import render
from django.views.generic import TemplateView

class Api(TemplateView):
    template_name = "templates/opo.html"
