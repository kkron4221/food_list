from food_list.models import FoodInfo
import re

# TOOD:delete table colum

def insert_colum(food_name, material_list):
    for i in range(len(material_list)):
        try:
            material = str(material_list[i][0])
            amount = re.sub(r"\D", "", material_list[i][1])
            unit = re.sub(r'\d', "", material_list[i][1])
        except:
            ValueError
            continue
        try:
            table_row = FoodInfo.objects.create(food_name=food_name, material=material, amount=amount, unit=unit)
            table_row.save()
        except:
            ValueError

# TODO:sort and add table colum
    
    return material_list