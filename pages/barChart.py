import streamlit as st
import matplotlib.pyplot as plt
import datetime
import pandas as pd

st.title("Calories Intake and Weight Tracker")

# define days of the week
day = st.date_input("Choose the days you want to track your weight and calories (minimum of 2 days) :", (datetime.date.today(), datetime.date(2024,4,21)),
    format="MM.DD.YYYY")

try:
# initalizes empty list for storing daily calorie intake
    calories_intake = []
    weight = []
    daterange = []
    days = pd.date_range(start=day[0], end=day[1])

# streamlit UI for user inpit

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

# show the plot
    st.pyplot(plt)

    plt.figure(figsize=(15, 6))
    st.write(days)
    plt.plot(daterange, weight, color='orange')

    plt.xlabel('Days of the Week')
    plt.ylabel('Weight (in lbs)')
    plt.title('Weight Changes per Day')

    st.pyplot(plt)

except Exception as e:
    st.warning("You need to select at least 2 days ")