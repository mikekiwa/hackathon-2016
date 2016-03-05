from django.http import HttpResponse
from django.shortcuts import render


def show_results(request):
    return HttpResponse('hello world')
