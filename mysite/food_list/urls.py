from django.urls import path
from . import views
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:title_text_id>/search/', views.search, name='search'),
  path('<int:title_text_id>/results/', views.results, name='results'),
]
