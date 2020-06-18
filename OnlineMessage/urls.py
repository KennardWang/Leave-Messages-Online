from django.conf.urls import url
from django.urls import path
from . import views, dbProcess, requestPost

urlpatterns = [
    # url(r'^hi/$', views.hello),
    path('messageBlock/', views.messageBlock),
    # path('requestGet/', requestGet.requestGet),
    path('response/', dbProcess.addData),
    path('board/', dbProcess.dataDisplay),
]