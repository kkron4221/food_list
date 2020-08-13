from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from selenium import webdriver
import time

def index(request):
  return HttpResponse(render(request, 'food_list/index.html'))
  
def results(request):
  food_name = request.POST.get('search1')
  url = "https://www.kurashiru.com/"

  driver = webdriver.Firefox()
  driver.get(url)
  search_box = driver.find_element_by_id("search_box")
  search_box.send_keys(Keys.ENTER, food_name)
  time.sleep(2)

  # item = driver.find_element_by_class_name("dly-video-item-root[1]")
  # item.click()
  # time.sleep(2)

  # materials = driver.find_element_by_class_name("ingredient-list-item")

  # return HttpResponse(materials)

  return HttpResponse(food_name)

  # params = {
  #   'food_name' : food_name,
  #   'material' : '卵',
  # }
  # return render(request, 'food_list/result.html', params)