import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

st.title("HCI Final Project about Health (Working title)")
#This is for the user to select their height
heightInFeet = st.selectbox("Select Height in Feet", (4, 5, 6, 7),index=None,placeholder= "Choose your height in Feet. eg, '5 foot' 8 inches")
heightInInches = st.selectbox("Select Height in Inches", (0,1,2,3,4,5,6,7,8,9,10,11),index=None,placeholder= "Choose your height in Inches. eg, 5 foot '8 inches'")

#This is for the user to input their weight
weightInPounds = st.number_input("Please enter your weight in pounds")

#This is the submit button, once the user hits the button it will do a try except condition where if the user does not
#select their height it will catch it and run a st.warning to explain to the user that they need to have both in order to
#run the program. If it doesn't catch the except then it runs the program normally
button= st.button("Submit", type="primary")
if button:
    try:
        #This is the math for the BMI calculator
        heightInTotal = (heightInFeet * 12) + heightInInches
        BMI = round((weightInPounds /heightInTotal/heightInTotal) * 703, 2)

        #This is to check within the ranges of the BMI. For example, if someone has a BMI of 17.3 it will display a
        #st.warning, not because they did something wrong but because they have to be careful about their weight, like
        #they have to gain more weight or lose more weight for the overweight BMI. If they exceed their BMI like having
        #a BMI of 45 it will throw a st.error because they really have to take care of their body. If they have a normal
        #BMI it will throw out the st.success since they do not have to worry about their weight.
        if 0 <= BMI <= 18.4:
            st.warning("Your BMI is " + str(BMI) + ", you are underweight (BMI: 0-18.4)")
            df = pd.read_csv("BMI Chart - Sheet1.csv")
            st.dataframe(df)

        if 18.5 <= BMI <= 24.9:
            st.success("Your BMI is " + str(BMI)+", you have a normal weight (BMI:18.5-24.9)")
            df = pd.read_csv("BMI Chart - Sheet1.csv")
            st.dataframe(df)

        if 25 <= BMI <= 29.9:
            st.warning("Your BMI is " + str(BMI) + ", you are overweight (BMI:25-29.9)")
            df = pd.read_csv("BMI Chart - Sheet1.csv")
            st.dataframe(df)

        if 30 <= BMI <= 10000:
            st.error("Your BMI is " + str(BMI) + ", you are obese (BMI:30-10000)")
            df = pd.read_csv("BMI Chart - Sheet1.csv")
            st.dataframe(df)
    except Exception as e:
        st.warning("You need to select a complete height in Feet or Inches")
