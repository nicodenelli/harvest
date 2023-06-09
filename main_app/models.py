from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Animal(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    preferred_living_conditions = models.CharField(max_length=250)
    user = models.ManyToManyField(User)


class Farm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    farm_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)


class Crop(models.Model):
    name = models.CharField(max_length=50)
    irrigation_needs = models.IntegerField()
    planting_season = models.CharField(max_length=50)
    hardiness_zone = models.CharField(max_length=100)
    maturity_days = models.IntegerField()
    user = models.ManyToManyField(User)


class Equipment(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    hydraulic_rating = models.IntegerField()
    year = models.IntegerField()
    color = models.CharField(max_length=20)
    description = models.TextField(max_length=250)
    engine_information = models.CharField(max_length=100)
    user = models.ManyToManyField(User)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, blank=True, null=True)
    crop = models.ForeignKey(
        Crop, on_delete=models.CASCADE, blank=True, null=True)
    equipment = models.ForeignKey(
        Equipment, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.CharField(max_length=150)
    date = models.DateField(auto_now=True)


class Photo(models.Model):
    url = models.CharField(max_length=200)
    animal = models.ForeignKey(
        Animal, on_delete=models.SET_NULL, blank=True, null=True)
    crop = models.ForeignKey(
        Crop, on_delete=models.SET_NULL, blank=True, null=True)
    equipment = models.ForeignKey(
        Equipment, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'Photo for animal_id {self.animal_id} @{self.url}'
