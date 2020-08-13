from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

def index(request):
  return HttpResponse(render(request, 'food_list/index.html'))
  
def results(request):
  food_name = request.POST.get('search1')
  url = "https://www.kurashiru.com/"

  options = Options()
  options.add_argument("-headless")

  driver = webdriver.Firefox(firefox_options=options)
  driver.get(url)
  time.sleep(2)
  search_box = driver.find_element_by_id("query")
  search_box.send_keys(food_name)
  search_box.send_keys(Keys.ENTER)
  time.sleep(2)

  items = driver.find_elements_by_class_name("dly-video-item-root")
  items[1].click()
  time.sleep(2)

  materials = driver.find_elements_by_class_name("ingredient-list-item")
  material_list = []
  for i in range(len(materials)):
    material_list.append(materials[i].text)

  params = {
    'food_name' : food_name,
    'materials' : material_list,
  }

  return render(request, 'food_list/result.html', params)