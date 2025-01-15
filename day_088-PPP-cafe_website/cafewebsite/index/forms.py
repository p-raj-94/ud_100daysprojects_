from django import forms
from cafe import models

class CreateCafe(forms.ModelForm):
    class Meta:
        model = models.Cafe
        fields = [
            'name',
            'map_url',
            'img_url',
            'location',
            'has_sockets',
            'has_toilet',
            'has_wifi',
            'can_take_calls',
            'seats',
            'coffee_price'
            ]