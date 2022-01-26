from api.models import *
import random

def generate():

    workout = {
        'category' : {
            'Upper Body Push': '',
            'Upper Body Pull': '',
            'Lower Body Push': '',
            'Lower Body Pull': '',
            'Core':''
        },
    }
    

    exercises = []

    # Basic logic for filtering later
    # for item in equipment:
    #     exercises.append(Exercise.objects.filter(category__name=category['category'], equipment__name=item))
    #     print(exercises)


    for category in workout['category']:
        exercises = Exercise.objects.filter(category__name=category)
        workout['category'][category] = str(random.choice(exercises))

    return workout





