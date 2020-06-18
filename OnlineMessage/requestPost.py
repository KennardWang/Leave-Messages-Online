from django.shortcuts import render
from django.views.decorators import csrf
from OnlineMessage import dbProcess as dbp
from Model.models import Data


def requestPost(request):
    display = []

    dbp.addData(request)

    Data.objects.order_by('mid')
    li = Data.objects.all()

    for item in li:
        display.append(item)

    return render(request, "error.html")
