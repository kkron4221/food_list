from django.db import models

class InputForm(models.Model):
  food_name = models.CharField(max_length=200)