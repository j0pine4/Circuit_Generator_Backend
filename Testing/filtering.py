exercises = [
    {
        'category' : 'UB_Push',
        'exercise' : 'Push Up',
        'equipment' : 'none',
        'MG' : ['chest', 'any' ]
    },
    {
        'category' : 'LB_Pull',
        'exercise' : 'Kettle Bell Swing',
        'equipment' : 'kettle-bell',
        'MG' : ['back', 'shoulders', 'legs', 'any']
    },
    {
        'category' : 'LB_Push',
        'exercise' : 'Kettle Bell Russian Twist',
        'equipment' : 'kettle-bell',
        'MG' : ['core', 'any']
    },
]

def filter(equipment, muscleGroup):

    mainList = []

    for exercise in exercises:
        if equipment in exercise['equipment'] and muscleGroup in exercise['MG']:
            mainList.append(exercise)

    print(mainList)


filter('kettle-bell', 'core')