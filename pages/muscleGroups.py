import random

# exercises per muscle group are defined
muscle_groups = {
    'arms' : ['bicep curls', 'hammer curls', 'tricep kickbacks', 'tricep dips' ],
    'back' : ['lateral pulldowns', 'seated rows' 'pull-ups', 'bent over rows'],
    'chest' : ['bench press', 'chest flye', 'push ups', 'chest press machine'],
    'shoulders' : ['shoulder press', 'dumbbell overhead press', 'lateral raises', 'front raises'],
    'glutes' : ['hip thrusts', 'squats', 'step-ups', 'cable kickbacks'],
    'legs' : ['romanian deadlifts', 'leg press', 'leg extentsions', 'hamstring curls'],
}

# function that generates the workout plan
def generate_plan(muscle_group, num_exercises = 4):
    if muscle_group.lower() not in muscle_groups:
        return "Invalid input, check your spelling and try again."
    exercises = random.sample(muscle_groups[muscle_group.lower()], min(num_exercises, len(muscle_groups[muscle_group.lower()])))
    return {muscle_group.lower(): exercises}                         
    
# fucntion that displays the workout plan
def display_plan(plan):
    for group, exercises in plan.items():
        print(f"{group.capitalize()} workout")
        for exercise in exercises:
            print(f" - {exercise}")
        print()

# usage and user input
if __name__ == "__main__":
    # prompts user to give input
    muscle_group = input("Enter the muscle group you want to work out (arms, back, chest, shoulders, glutes, legs):")
    num_per_group = int(input("Enter the number of exercises you want for your chosen muscle groups:"))

    #generate plan based on muscle group input
    plan = generate_plan(muscle_group, num_per_group)

    # display
    if isinstance(plan, dict):
        display_plan(plan)
    else:
        print(plan)