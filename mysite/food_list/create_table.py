from food_list.models import FoodInfo

def insert_colum(food_name, material_list):
    for i in range(len(material_list)):
        table_row = FoodInfo.objects.create(food_name=food_name, material=material_list[i][0], amount=1, unit="hogehoge")    
    table_row.save()
    return material_list