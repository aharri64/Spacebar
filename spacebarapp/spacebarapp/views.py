from django.views.generic import TemplateView
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')
