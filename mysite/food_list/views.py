from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.urls import reverse



def index(request):
  return render(request, 'food_list/index.html')
  
# search material from api
def search(request):
  return HttpResponse("hogehoge")

def results(request):
  params = {
    'food_name' : request.POST.get('search'),
    'material' : '卵',
  }
  return render(request, 'food_list/result.html', params)