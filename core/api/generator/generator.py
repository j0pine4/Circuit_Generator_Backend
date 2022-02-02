from api.models import *
import random

def generate():

    workout = {
        'category' : {
            'Upper Body Push': {
                'id': '',
                'name': ''
            },
            'Upper Body Pull': {
                'id': '',
                'name': ''
            },
            'Lower Body Push': {
                'id': '',
                'name': ''
            },
            'Lower Body Pull': {
                'id': '',
                'name': ''
            },
            'Core':{
                'id': '',
                'name': ''
            }
        },
    }
    

    exercises = []

    # Basic logic for filtering later
    # for item in equipment:
    #     exercises.append(Exercise.objects.filter(category__name=category['category'], equipment__name=item))
    #     print(exercises)


    for category in workout['category']:
        exercises = Exercise.objects.filter(category__name=category).values_list('id', 'name')
        exercise = random.choice(exercises)
        workout['category'][category]['id'] = exercise[0]
        workout['category'][category]['name'] = exercise[1]

    return workout





