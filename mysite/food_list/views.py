from django.http import HttpResponse
from django.shortcuts import render
from . import search_material
from . import create_table

def index(request):
  return HttpResponse(render(request, 'food_list/index.html'))
  
def results(request):
  foods_list = []
  materials_list = []
  i = "1"
  search_food = "search" + i
  food_name = request.POST.get(search_food)
  foods_list.append(food_name)
  material_list = search_material.selenium_function(food_name)
  materials_list.append(material_list)
  create_table.insert_colum(food_name, material_list)

  params = {
    'days' : 3,
    'food_names' : foods_list,
    'materials' : materials_list,
  }



  return render(request, 'food_list/result.html', params)
  