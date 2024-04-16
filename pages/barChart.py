import streamlit as st
import matplotlib.pyplot as plt
import datetime
import pandas as pd

st.title("Calories Intake and Weight Tracker")

# define what days the user is going to select
day = st.date_input("Choose the days you want to track your weight and calories (minimum of 2 days) :", (datetime.date.today(), datetime.date(2024,4,21)),
    format="MM.DD.YYYY")

#If this catches the execption of not having more than 2 days it will give out a st.warning, advising them to select more than one day
try:
# initalizes empty list for storing daily calorie intake, weight, and the range of the days
    calories_intake = []
    weight = []
    daterange = []
    days = pd.date_range(start=day[0], end=day[1])

# streamlit UI for user input

    st.write("Enter your calories for each day of the week: ")

    for day in days:

        calorie_input = st.number_input(f"Enter calorie for {day.month}.{day.day}.{day.year}",min_value=300)
        weight_input = st.number_input(f"Enter weight for {day.month}.{day.day}.{day.year}",min_value=0)
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
    plt.title('Calories Intake per Day')

# show the bar to the user
    st.pyplot(plt)

#creates the line chart
    plt.figure(figsize=(15, 6))
    st.write(days)
    plt.plot(daterange, weight, color='orange')

# add labels and title
    plt.xlabel('Days of the Week')
    plt.ylabel('Weight (in lbs)')
    plt.title('Weight Changes per Day')

#show the line chart to the user
    st.pyplot(plt)

except Exception as e:
    st.warning("You need to select at least 2 days ")