from django.db import models

class FoodInfo(models.Model):
  food_name = models.CharField(max_length=200)
  material = models.CharField(max_length=200)
  amount = models.IntegerField()
  unit = models.CharField(max_length=200)