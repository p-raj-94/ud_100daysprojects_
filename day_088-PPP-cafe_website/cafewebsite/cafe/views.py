from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Cafe
# Create your views here.

def api_get_cafes(request):
    cafes = Cafe.objects.all().order_by("name")
    json = serializers.serialize("json", cafes)
    return HttpResponse(json)