from django.shortcuts import render

from lights.models import LightSample


def show_results(request):
    samples = LightSample.objects.order_by('-created_date')[:50]
    return render(request, 'results.html', {'samples': samples})
