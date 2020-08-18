from django.http import HttpResponse
from django.shortcuts import render
from . import search_material

def index(request):
  return HttpResponse(render(request, 'food_list/index.html'))
  
def results(request):
  food_name = request.POST.get('search1')
  material_list = search_material.selenium_function(food_name)



  params = {
    'food_name' : food_name,
    'materials' : material_list,
  }

  return render(request, 'food_list/result.html', params)