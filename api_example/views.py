from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def names(request):
    data={'names': ['William', 'Rod', 'Grant']}
    return JsonResponse(data)


