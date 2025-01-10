from django.urls import path
from . import views

app_name = 'cafe'

urlpatterns = [
    path('getcafes', views.api_get_cafes)
]