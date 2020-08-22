import sqlite3
from food_list.models import FoodInfo

food_name = "寿司"
material_list = ["白米", "刺身", "山葵"]

for i in range(len(material_list)):
    table_row = FoodInfo.objects.create(food_name=food_name, material=material_list[i][0], amount=1, unit="hogehoge")
table_row.save()

FoodInfo.objects.filter(food_name).order_by()