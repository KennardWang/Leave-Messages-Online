
from django.http import HttpResponse
from django.shortcuts import render


def requestGet(request):
    request.encoding = 'utf-8'
    if 'mes' in request.GET and request.GET['mes']:
        message = '你搜索的内容为: ' + request.GET['mes']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)