from django.db import models

# Create your models here.

class resto(models.Model):
    rid = models.IntegerField()
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    items = models.CharField(max_length=500)
    lat_long = models.CharField(max_length=100)
    full_details = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class dish(models.Model):
    did = models.IntegerField()
    dish = models.CharField(max_length=500)
    mrp = models.CharField(max_length=500)
    def __str__(self):
        return self.dish
