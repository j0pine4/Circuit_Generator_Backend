from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.db.models.fields import CharField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class MuscleGroup(models.Model):
    name = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.name

class equipment(models.Model):
    name = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=CASCADE, null=True)
    muscleGroup = models.ManyToManyField(MuscleGroup)
    equipment = models.ManyToManyField(equipment)

    def __str__(self):
        return self.name


class Workout(models.Model):
    exercise = models.ManyToManyField(Exercise)

    def __str__(self):
        return str(self.id)

