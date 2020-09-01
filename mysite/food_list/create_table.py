from food_list.models import FoodInfo
import re

def insert_colum(food_name, material_list):
    for i in range(len(material_list)):
        try:
            material = material_list[i][0]
            amount = re.sub('\\D', "", material_list[i][1])
            amount = int(amount)
            unit = re.sub('[0-9０-９]+', "", material_list[i][1])
        except:
            ValueError
            continue
        table_row = FoodInfo.objects.create(food_name=food_name, material=material, amount=amount, unit=unit)

# TODO:sort and add table colum
    
    return material_list