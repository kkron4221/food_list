# from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from urllib import request
from bs4 import BeautifulSoup
import time

def selenium_function(food_name):
    url = "https://www.kurashiru.com/"
    material_list = []
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
    items[0].click()
    time.sleep(2)

    food_url = driver.current_url

    html = request.urlopen(food_url)

    soup = BeautifulSoup(html, "html.parser")

    material_info = soup.find_all("li", class_="ingredient-list-item")

    for i in material_info:
        material = i.text
        if " " in material:
            material = material.split()
        else:
            continue
        material_list.append(material)

    return material_list, food_url