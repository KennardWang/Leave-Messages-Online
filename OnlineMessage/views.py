
from django.http import HttpResponse
from django.shortcuts import render

def messageBlock(request):
    return render(request, 'form.html')

def test(request):
    context = {}
    context['hi'] = 'Hello'
    return render(request, 'error.html', context)
