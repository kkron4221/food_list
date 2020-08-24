from food_list.models import FoodInfo
import re

# TOOD:delete table colum

def insert_colum(food_name, material_list):
    for i in range(len(material_list)):
        try:
            material_list[i][1]  = str(material_list[i][1])
            amount = re.sub('\\D', "", material_list[i][1])
            unit = re.sub('[0-9０-９]+', "", material_list[i][1])
        except:
            ValueError
            break
        try:
            table_row = FoodInfo.objects.create(food_name=food_name, material=material_list[i][0], amount=amount, unit=unit)
            table_row.save()
        except:
            ValueError

# TODO:sort and add table colum
    
    return material_list