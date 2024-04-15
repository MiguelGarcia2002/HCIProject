import streamlit as st
import random

# exercises per muscle group are defined
muscle_groups = {
    'arms': ['bicep curls', 'hammer curls', 'tricep kickbacks', 'tricep dips'],
    'back': ['lateral pulldowns', 'seated rows', 'pull-ups', 'bent over rows'],
    'chest': ['bench press', 'chest flye', 'push ups', 'chest press machine'],
    'shoulders': ['shoulder press', 'dumbbell overhead press', 'lateral raises', 'front raises'],
    'glutes': ['hip thrusts', 'squats', 'step-ups', 'cable kickbacks'],
    'legs': ['romanian deadlifts', 'leg press', 'leg extensions', 'hamstring curls'],
}

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
def main():
    st.title("Workout Planner")
    st.sidebar.title("Input")

    # user input for muscle group
    muscle_group = st.sidebar.selectbox("Select your preferred muscle group", list(muscle_groups.keys()))
    
    # user input for number of exercises
    num_exercises = st.sidebar.number_input("Enter the number of exercises you want for your chosen muscle group: ", min_value=1, max_value=len(muscle_groups[muscle_group]), value=len(muscle_groups[muscle_group]))

    # generates and displays the workout plan
    plan = generate_plan(muscle_group, num_exercises)
    if isinstance(plan, dict):
        display_plan(plan)
    else:
        st.error(plan)

if __name__ == "__main__":
    main()
