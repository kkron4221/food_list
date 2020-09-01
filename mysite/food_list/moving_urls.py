from django.http import HttpResponse
from django.shortcuts import render


def transition(request):
    # when click img
    url = ""

    return HttpResponse(render(request, url))