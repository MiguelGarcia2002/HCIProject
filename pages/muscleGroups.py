import streamlit as st
import random
import requests

APIkey = "CSubUG2QXR5ECIaeCoChAA==rXIcnOjUmlQ8eRLn"

st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"]::before {
            content: "Fitness Buddy API";
            margin-left: 20px;
            margin-top: 20px;
            font-size: 30px;
            position: relative;
            top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# exercises per muscle group are defined
muscle_groups = {
    # 'arms': ['bicep curls', 'hammer curls', 'tricep kickbacks', 'tricep dips'],
    # 'back': ['lateral pulldowns', 'seated rows', 'pull-ups', 'bent over rows'],
    'chest': ['bench press', 'chest flye', 'push ups', 'chest press machine'],
    # 'shoulders': ['shoulder press', 'dumbbell overhead press', 'lateral raises', 'front raises'],
    'glutes': ['hip thrusts', 'squats', 'step-ups', 'cable kickbacks'],
    # 'legs': ['romanian deadlifts', 'leg press', 'leg extensions', 'hamstring curls'],
}

muscle = 'biceps'


# if response.status_code == requests.codes.ok:
#     print("response works")
# else:
#     print("Error:", response.status_code, response.text)


# function that generates the workout plan
def generate_plan(muscle_group, num_exercises=4):
    if muscle_group.lower() not in muscle_groups:
        return "Invalid input, check your spelling and try again."
    exercises = random.sample(muscle_groups[muscle_group.lower()],
                              min(num_exercises, len(muscle_groups[muscle_group.lower()])))
    return {muscle_group.lower(): exercises}


# function that displays the workout plan
def display_plan(plan):
    for group, exercises in plan.items():
        st.subheader(f"{group.capitalize()} workout")
        for exercise in exercises:
            st.write(f" - {exercise}")


# streamlit UI
st.title("Workout Planner")
# st.title("Input")

# user input for muscle group
muscle_group = st.selectbox("Select your preferred muscle group", list(muscle_groups.keys()))

# user input for number of exercises
# num_exercises = st.number_input("Enter the number of exercises you want for your chosen muscle group: ", min_value=1,
#                                 max_value=len(muscle_groups[muscle_group]),
#                                 value=len(muscle_groups[muscle_group]))

# User input for difficulty of exercise
exercise_difficulty = st.radio("Select level of difficulty for the exercise: ",
                               options=["beginner", "intermediate", "expert"]
                               )

# generates and displays the workout plan
api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle_group)
response = requests.get(api_url, headers={'X-Api-Key': APIkey})
if response.status_code == requests.codes.ok:
    data = response.json()
    # st.write(data)
    checkArray = []
    for i in data:
        if i["difficulty"] == exercise_difficulty:
            checkArray.append(i)
    if len(checkArray) == 0:
        st.error("There aren't any exercise for the given difficulty, please select a different difficulty")
    else:
        num_exercises = st.number_input("Enter the number of exercises you want for your chosen muscle group: ",
                                        min_value=1, max_value=len(checkArray))
        for i in range(num_exercises):
            exercise_name = data[i]["name"]
            #         exercise_name = i["name"]
            #         exercise_equipment = i["equipment"]
            #         exercise_description = i["instructions"]
            st.write(exercise_name)
    #         st.write(exercise_equipment)
    #         st.write(exercise_description)
    #
    # if len(checkArray) == 0:
    #     st.warning("There aren't any exercise for the given difficulty, please select a different difficulty")
    # else:
else:
    st.error("Error with the API request, please try again later!")


