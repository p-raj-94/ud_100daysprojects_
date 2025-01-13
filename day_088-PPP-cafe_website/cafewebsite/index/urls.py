from django.urls import include, path

from . import views

app_name = 'index'

urlpatterns = [
    path("", views.index, name="index"),
    path("add_cafe", views.add_cafe, name="add_cafe")
]