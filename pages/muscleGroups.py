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
    'chest': ['bench press', 'chest flye', 'push ups', 'chest press machine'],
    'glutes': ['hip thrusts', 'squats', 'step-ups', 'cable kickbacks'],
    'neck' : [],
    'traps': [],
    'abdominals': [],
    'abductors': [],
    'adductors': [],
    'biceps': [],
    'calves':[],
    'forearms': [],
}



# streamlit UI
st.title("Workout Planner")
st.markdown("This planner will allow you to select a group of muscle that you wanna work out on and then select the amount of exercises you wanna do, it will then allow you to see how to do those exercises using the dropdown menu")

# user input for muscle group
muscle_group = st.selectbox("Select your preferred muscle group", list(muscle_groups.keys()))


# User input for difficulty of exercise
exercise_difficulty = st.radio("Select level of difficulty for the exercise: ",
                               options=["beginner", "intermediate", "expert"]
                               )

# generates and displays the workout plan
api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle_group)
response = requests.get(api_url, headers={'X-Api-Key': APIkey})
if response.status_code == requests.codes.ok:
    data = response.json()
    checkArray = []
    for i in data:
        if i["difficulty"] == exercise_difficulty:
            checkArray.append(i)
    if len(checkArray) == 0:
        st.error("There aren't any exercise for the given difficulty, please select a different difficulty")
    else:
        num_exercises = st.number_input("Enter the number of exercises you want for your chosen muscle group: ",
                                        min_value=1, max_value=len(checkArray))
        st.header("Chose an exercise:")
        exercise_names = [exercise["name"] for exercise in checkArray[:num_exercises]]
        exercise = st.selectbox("Select the Exercise", exercise_names)
        for i in data:
            if i["name"] == exercise:
                print(i)
                exercise_name = i["name"]
                st.title(exercise_name)
                st.header("Required Material:")
                st.subheader(i["equipment"])
                st.header("Instructions:")
                st.write(i["instructions"])
else:
    st.error("Error with the API request, please try again later!")


