from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
  num = list(range(10))
  context = {'num_list' : num}
  return HttpResponse(render(request, 'food_list/index.html', context))
  
def results(request):
  params = {
    'food_name' : request.POST.get('search'),
    'material' : '卵',
  }
  return render(request, 'food_list/result.html', params)