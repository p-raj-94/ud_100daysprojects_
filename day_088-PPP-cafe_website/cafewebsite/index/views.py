from django.shortcuts import render, redirect
from django.http import HttpResponse
from cafe.models import Cafe
from . import forms

# Create your views here.
def index(request):
    cafes = Cafe.objects.all()
    locations = [ cafe.map_url for cafe in cafes]
    return render(request, 'home.html', { 'cafes': cafes, 'locations': locations})

def add_cafe(request):
    if request.method == 'POST':
        form = forms.CreateCafe(request.POST)
        if form.is_valid():
            new_cafe = form.save(commit=False)
            new_cafe.save()
            return redirect('index:index')
    else:
        form = forms.CreateCafe()

    
    return render(request, 'add_cafe.html', {'form': form})