import data
import screenDisplay


def workout(allWorkouts, incompleteWorkouts):

    print(len(data.WorkoutDictionary.allWorkouts))
    if len(incompleteWorkouts) == 0:
        data.generateWorkout(data.WorkoutDictionary.allWorkouts, data.WorkoutDictionary.incompleteWorkouts)


# Initiates Program
def programInit():

    # Imports all workouts from CSV file. Stores in data.AllWorkoutLists
    data.importAllWorkouts(data.WorkoutDictionary.allWorkouts)
