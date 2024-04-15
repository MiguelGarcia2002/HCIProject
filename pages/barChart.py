import streamlit as st
import matplotlib.pyplot as plt

# define days of the week
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# initalizes empty list for storing daily calorie intake
calories_intake = []

# streamlit UI for user inpit
st.title("Calories Intake Tracker")
st.write("Enter your calories for each day of the week: ")

for day in days:
    calorie_input = st.number_input(f"Enter calorie for {day}", min_value = 1200)
    calories_intake.append(calorie_input)

# create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(days, calories_intake, color='skyblue')

# add labels and title
plt.xlabel('Days of the Week')
plt.ylabel('Calories Intake')
plt.title('Calories Intake per Day of the Week')

# show the plot
st.pyplot(plt)