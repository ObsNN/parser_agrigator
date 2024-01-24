from django.urls import URLPattern, path
from .views import *
from django.http import JsonResponse

urlpatterns = [
    path('', indexMouses),
    path('article/<int:articleId>/',indexArticles),
    path('data/',getData),
    path('data2/',getDataDns)
]
