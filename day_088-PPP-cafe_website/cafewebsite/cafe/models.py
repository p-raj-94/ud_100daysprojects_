from django.db import models

# Create your models here.
class Cafe(models.Model):
    name = models.CharField(unique=True, max_length=250)
    map_url = models.CharField(max_length=500)
    img_url = models.CharField(max_length=500)
    location = models.CharField(max_length=250)
    has_sockets = models.BooleanField()
    has_toilet = models.BooleanField()
    has_wifi = models.BooleanField()
    can_take_calls = models.BooleanField()
    seats = models.CharField(blank=True, null=True, max_length=200)
    coffee_price = models.CharField(blank=True, null=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'cafe'