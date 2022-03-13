from django.db.models.query import QuerySet
from django.shortcuts import render

from .models import *
from .serializers import *
from rest_framework import viewsets
import json

from api.generator.generator import generate, exerciseList, customWorkout
from rest_framework.decorators import api_view
from django.http import HttpResponse

# Create your views here.
class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ReadExerciseSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset =  Workout.objects.all()
    serializer_class = ReadWorkoutSerializer

class MuscleGroupsViewSet(viewsets.ModelViewSet):
    queryset =  MuscleGroup.objects.all()
    serializer_class = MuscleGroupSerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset =  equipment.objects.all()
    serializer_class = EquipmentSerializer

# Generator View
@api_view(["GET", "POST"])
def runMe(request):

    # For Filtering Tests
    # generate(['dumbbell', 'kettle_bell'])

    if request.method == "POST":
        workout = customWorkout(equipmentList=['body_weight', 'kettle_bell'])
        return HttpResponse(json.dumps(workout))
        # return HttpResponse("Hello")

    workout = generate()
    return HttpResponse(json.dumps(workout))

# Generator View
@api_view(["GET", "POST"])
def exerciseListView(request):


    list = exerciseList()
    return HttpResponse(json.dumps(list))

