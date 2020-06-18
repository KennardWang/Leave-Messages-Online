
from django.http import HttpResponse
from Model.models import Data
from django.shortcuts import render

def addData(request):

    nick = request.POST['nickname']
    cont = request.POST['mes']

    if len(nick) == 0 or len(cont) == 0:
        return render(request, "error.html")
    else:
        Data(nickname=nick, content=cont).save()
        return render(request, "response.html")

def dataDisplay(request):
    display = []
    Data.objects.order_by('mid')
    li = Data.objects.all()

    for item in li:
        display.append(item)

    return render(request, "board.html", {"display": display})


