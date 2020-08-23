from django.http import HttpResponse
from django.shortcuts import render
from .models import FoodInfo
from . import search_material
from . import create_table

def index(request):
  return HttpResponse(render(request, 'food_list/index.html'))
  
def results(request):
  foods_list = []
  materials_list = []
  url_list = []
 
  for i in range(10):
    i = i + 1
    search_food = "search" + str(i) 
    food_name = request.POST.get(search_food)
    if food_name == "":
      break
    foods_list.append(food_name)
    food_selenium = search_material.selenium_function(food_name)
    material_list = food_selenium[0]
    menu_url = food_selenium[1]
    materials_list.append(material_list)
    url_list.append(menu_url)
    create_table.insert_colum(food_name, material_list)
    days = i

  allfoods = FoodInfo.objects.all()
  sorted_foods_material = sorted(allfoods, key=lambda food:food.material)  

  context = {'allfoods':allfoods,
            'sorted_food_material':sorted_foods_material,
            'days':days,
            'url_list':url_list
            }



  return render(request, 'food_list/result.html', context)