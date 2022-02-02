from unicodedata import category
from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )

class MuscleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleGroup
        fields = (
            'id',
            'name',
        )

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = equipment
        fields = (
            'id',
            'name',
        )


class ReadExerciseSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    muscleGroup = MuscleGroupSerializer(many=True)

    class Meta:
        model = Exercise
        fields = (
            'id',
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
            'id',
            'exercise',
        )
