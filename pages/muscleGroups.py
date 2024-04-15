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
def generate_plan(num_per_group = 4):
    plan = {}
    for group, exercises in muscle_groups.items():
        plan[group] = random.sample(exercises, num_per_group)
    return plan

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
    num_per_group = int(input("Enter the desired muscle group you would like to workout: "))

    #generate plan based on muscle group input
    plan = generate_plan(num_per_group)

    # display
    display_plan(plan)