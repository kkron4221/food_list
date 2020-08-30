from food_list.models import FoodInfo
import re

# TOOD:delete table colum

def insert_colum(food_name, material_list):
    for i in range(len(material_list)):
        try:
<<<<<<< HEAD
            material_list[i][1]  = str(material_list[i][1])
            amount = re.sub('\\D', "", material_list[i][1])
            unit = re.sub('[0-9０-９]+', "", material_list[i][1])
            if unit == "大さじ":
                unit = "小さじ"
                amount = int(amount) * 3
            if unit == "/本":
                unit = "個"
            if unit == "合":
                unit = "150g"
=======
            material = str(material_list[i][0])
            amount = re.sub(r"\D", "", material_list[i][1])
            unit = re.sub(r'\d', "", material_list[i][1])
>>>>>>> 0036a2876ac30d53015612291e0a7be03fb6d1ed
        except:
            ValueError
            continue
        try:
            table_row = FoodInfo.objects.create(food_name=food_name, material=material, amount=amount, unit=unit)
            table_row.save()
        except:
            ValueError
            continue

# TODO:sort and add table colum
    
    return material_list