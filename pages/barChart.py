import streamlit as st
import matplotlib.pyplot as plt
import datetime
import pandas as pd
from datetime import timedelta

n = 0
# define days of the week
day = st.date_input("Choose the days you want to track your weight and calories (minuium of 3 days) :", (datetime.date(2024,1,1), datetime.date(2024, 1, 7)),
    format="MM.DD.YYYY")


# initalizes empty list for storing daily calorie intake
calories_intake = []
weight = []
daterange = []
days = pd.date_range(start=day[0], end=day[1])

# streamlit UI for user inpit
st.title("Calories Intake Tracker")
st.write("Enter your calories for each day of the week: ")

for day in days:

    calorie_input = st.number_input(f"Enter calorie for {day.month}.{day.day}.{day.year}",value = None ,placeholder="1200")
    weight_input = st.number_input(f"Enter weight for {day.month}.{day.day}.{day.year}",Value =None ,placeholder="1200")
    st.write("   ")
    calories_intake.append(calorie_input)
    weight.append(weight_input)
    date = f"{day.month}.{day.day}.{day.year}"
    daterange.append(date)

# create the bar chart
plt.figure(figsize=(15, 6))
st.write(days)
plt.bar(daterange, calories_intake, color='skyblue')

# add labels and title
plt.xlabel('Days of the Week')
plt.ylabel('Calories Intake')
plt.title('Calories Intake per Day of the Week')

# show the plot
st.pyplot(plt)