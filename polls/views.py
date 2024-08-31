from django.shortcuts import render # type: ignore

# Create your views here.

from django.http import HttpResponse # type: ignore


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
