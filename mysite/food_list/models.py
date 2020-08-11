from django.db import models

class Title(models.Model):
  title_text = models.CharField(max_length=200)
