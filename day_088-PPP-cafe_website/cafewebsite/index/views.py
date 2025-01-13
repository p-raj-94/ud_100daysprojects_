from django.shortcuts import render
from django.http import HttpResponse
from cafe.models import Cafe

# Create your views here.
def index(request):
    cafes = Cafe.objects.all()
    return render(request, 'home.html', { 'cafes': cafes})

def add_cafe(request):
    return render(request, 'add_cafe.html')