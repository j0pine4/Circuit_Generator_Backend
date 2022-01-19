from unicodedata import category
from api.models import *
import random

def generate():

    categories = [
        {'category' : 'Upper Body Push'},
        {'category' : 'Upper Body Pull'},
        {'category' : 'Lower Body Push'},
        {'category' : 'Lower Body Pull'},
        {'category' : 'Core'},
    ]

    workout = {
        'Upper Body Push' : '',
        'Upper Body Pull' : '',
        'Lower Body Push' : '',
        'Lower Body Pull' : '',
        'Core' : '',
    }

    exercises = []

    for category in categories:
        exercises = Exercise.objects.filter(category__name=category['category'])
        workout[category['category']] = str(random.choice(exercises))

        # for item in equipment:
        #     exercises.append(Exercise.objects.filter(category__name=category['category'], equipment__name=item))
        #     print(exercises)


    return workout
    print(exercises)





