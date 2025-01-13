from django.urls import include, path

from . import views

app_name = 'index'

urlpatterns = [
    path("", views.index, name="index"),
]