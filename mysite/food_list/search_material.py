from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

def selenium_function(food_name):
    url = "https://www.kurashiru.com/"
    material_info = [] 
    options = Options()
    options.add_argument("-headless")

    driver = webdriver.Firefox(firefox_options=options)
    driver.get(url)
    time.sleep(2)
    search_box = driver.find_element_by_id("query")

    search_box.send_keys(food_name)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

    img = driver.find_elements_by_tag_name("img")
    target_img = img[0]
    time.sleep(1)

    items = driver.find_elements_by_class_name("dly-video-item-root")
    items[0].click()
    time.sleep(2)

    materials = driver.find_elements_by_class_name("ingredient-list-item")
    # materials.append(target_img)
    food_url = driver.current_url
    material_list = []
    for i in range(len(materials)):
        material_info = materials[i].text.splitlines()
        if len(material_info) < 2:
            continue
        material_list.append(material_info)

    return material_list, food_url