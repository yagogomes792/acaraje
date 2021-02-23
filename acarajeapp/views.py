from django.shortcuts import render, redirect, HttpResponse
from .models import Cardapio

# Create your views here.

def index(request):
    data = {}
    data['cardapio'] = Cardapio.objects.all()
    return render(request,'index.html', data)



