from django.shortcuts import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Title


def index(request):

  return render(request, 'food_list/index.html')
  
def search(request):
  return HttpResponse("Now searching")

def results(request, title_text_id):
  return HttpResponse("Result" + title_text_id + "food")
