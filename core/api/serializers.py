from unicodedata import category
from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
        )

class MuscleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleGroup
        fields = (
            'name',
        )


class ReadExerciseSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    muscleGroup = MuscleGroupSerializer(many=True)

    class Meta:
        model = Exercise
        fields = (
            'name',
            'category',
            'muscleGroup'
        )

class ReadWorkoutSerializer(serializers.ModelSerializer):
    
    #Foreign Serializer
    exercise = ReadExerciseSerializer(many=True)

    class Meta:
        model = Workout
        fields = (
            'exercise',
        )
