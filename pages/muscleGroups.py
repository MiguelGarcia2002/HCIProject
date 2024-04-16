import streamlit as st
import random
import requests

# exercises per muscle group are defined
muscle_groups = {
    'arms': ['bicep curls', 'hammer curls', 'tricep kickbacks', 'tricep dips'],
    'back': ['lateral pulldowns', 'seated rows', 'pull-ups', 'bent over rows'],
    'chest': ['bench press', 'chest flye', 'push ups', 'chest press machine'],
    'shoulders': ['shoulder press', 'dumbbell overhead press', 'lateral raises', 'front raises'],
    'glutes': ['hip thrusts', 'squats', 'step-ups', 'cable kickbacks'],
    'legs': ['romanian deadlifts', 'leg press', 'leg extensions', 'hamstring curls'],
}


APIkey = "CSubUG2QXR5ECIaeCoChAA==rXIcnOjUmlQ8eRLn"

muscle = 'biceps'
api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle)
response = requests.get(api_url, headers={'X-Api-Key': APIkey})
if response.status_code == requests.codes.ok:
    print("response works")
else:
    print("Error:", response.status_code, response.text)


# function that generates the workout plan
def generate_plan(muscle_group, num_exercises=4):
    if muscle_group.lower() not in muscle_groups:
        return "Invalid input, check your spelling and try again."
    exercises = random.sample(muscle_groups[muscle_group.lower()], min(num_exercises, len(muscle_groups[muscle_group.lower()])))
    return {muscle_group.lower(): exercises}                         
    
# function that displays the workout plan
def display_plan(plan):
    for group, exercises in plan.items():
        st.subheader(f"{group.capitalize()} workout")
        for exercise in exercises:
            st.write(f" - {exercise}")

# streamlit UI
st.title("Workout Planner")
st.sidebar.title("Input")

    # user input for muscle group
muscle_group = st.selectbox("Select your preferred muscle group", list(muscle_groups.keys()))
    
    # user input for number of exercises
num_exercises = st.number_input("Enter the number of exercises you want for your chosen muscle group: ", min_value=1, max_value=len(muscle_groups[muscle_group]), value=len(muscle_groups[muscle_group]))

    # generates and displays the workout plan
plan = generate_plan(muscle_group, num_exercises)
if isinstance(plan, dict):
    display_plan(plan)
else:
    st.error(plan)


