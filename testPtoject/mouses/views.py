from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from .parser import parseDns

# Create your views here.
def indexMouses(request):
    return HttpResponse('Страница мышей')

def indexArticles(request,articleId):
    return HttpResponse(f"<h1>Статьи с номером -  {articleId}</h1>")

def getData(request):
    data = {
        "Ключь":"1",
        "Ключь2":"7"
    }
    print(data)
    return JsonResponse(data)

def getDataDns(request):
    par = parseDns()
    print(123123,par)
    return HttpResponse(par)
    