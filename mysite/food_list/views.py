from django.http import HttpResponse
from django.shortcuts import render
from .models import FoodInfo
from . import search_material
from . import create_table
from django.db.models import Sum

def index(request):
  return HttpResponse(render(request, 'food_list/index.html'))
  
def results(request):
  FoodInfo.objects.all().delete()
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
    foods_url = food_selenium[1]
    create_table.insert_colum(food_name, material_list)
    materials_list.append(material_list)
    days = i
<<<<<<< HEAD

  result_info = FoodInfo.objects.values('material', 'unit').order_by('material').annotate(amount=Sum('amount'))

  context = {
            'result_info':result_info,
            'foods_list':foods_list,
=======
  
  allfoods = FoodInfo.objects.all()
  sorted_foods_material = sorted(allfoods, key=lambda FoodInfo:FoodInfo.material)  

  context = {
            'allfoods':allfoods,
            'sorted_foods_material':sorted_foods_material,
>>>>>>> 0036a2876ac30d53015612291e0a7be03fb6d1ed
            'days':days,
            }

<<<<<<< HEAD
=======

>>>>>>> 0036a2876ac30d53015612291e0a7be03fb6d1ed
  return render(request, 'food_list/result.html', context)