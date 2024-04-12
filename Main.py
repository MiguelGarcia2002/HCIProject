import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("HCI Final Project about Health (Working title)")

heightInFeet = st.selectbox("Select Height in Feet", (4, 5, 6, 7),placeholder= "Choose your height in Feet. eg '5 foot' 8 inches")
heightInInches = st.selectbox("Select Height in Inches", (0,1,2,3,4,5,6,7,8,9,10,11),placeholder= "Choose your height in Inches. eg 5 foot '8 inches'")


weightInPounds = st.number_input("Please enter your weight in pounds")

heightInFeet = int(heightInFeet)
heightInInches = int(heightInInches)
heightInTotal = (heightInFeet * 12) + heightInInches

BMI =(weightInPounds /heightInTotal/heightInTotal) * 703


if 0.1 <= BMI <= 18:
    st.warning("Your BMI is " + str(BMI) + ", you are underweight")
    df = pd.read_csv("BMI Chart - Sheet1 (1).csv")
    filtered_df = df[df['Ft In'] == f"{heightInFeet}'{heightInInches}\""]
    st.dataframe(filtered_df)

if 19 <= BMI <= 24:
    st.success("Your BMI is " + str(BMI)+", you have a normal weight")
    df = pd.read_csv("BMI Chart - Sheet1 (1).csv")
    st.dataframe(df)

if 25 <= BMI <= 30:
    st.warning("Your BMI is " + str(BMI) + ", you are overweight")
    df = pd.read_csv("BMI Chart - Sheet1 (1).csv")
    st.dataframe(df)

if 30 <= BMI <= 10000:
    st.error("Your BMI is " + str(BMI) + ", you are obese")
    df = pd.read_csv("BMI Chart - Sheet1 (1).csv")
    st.dataframe(df)

