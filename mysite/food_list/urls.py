from django.urls import path, include
from . import views

app_name = 'food_list'
urlpatterns = [
  path('', views.index, name='index'),
  path('search/', views.search, name='search'),
  path('results/', views.results, name='results'),
]
