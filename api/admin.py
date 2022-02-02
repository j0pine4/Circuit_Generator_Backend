from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Exercise)
admin.site.register(equipment)
admin.site.register(MuscleGroup)
admin.site.register(Workout)