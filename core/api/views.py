from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
import json

from api.generator.generator import generate
from rest_framework.decorators import api_view
from django.http import HttpResponse

# Create your views here.
class ExerciseViewSet(viewsets.ModelViewSet):

    queryset = Exercise.objects.all()
    serializer_class = ReadExerciseSerializer

class WorkoutViewSet(viewsets.ModelViewSet):

    queryset =  Workout.objects.all()
    serializer_class = ReadWorkoutSerializer

# Generator View
@api_view(["GET", "POST"])
def runMe(request):

    # Testing a new branch for filtering

    # For Filtering Tests
    # generate(['dumbbell', 'kettle_bell'])

    if request.method == "POST":
        return HttpResponse("Workout Test")

    workout = generate()
    return HttpResponse(json.dumps(workout))

