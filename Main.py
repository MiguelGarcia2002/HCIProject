import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("HCI Final Project about Health (Working title)")

heightInFeet = st.selectbox("Select Height in Feet", (4, 5, 6, 7),index=None,placeholder= "Choose your height in Feet. eg, '5 foot' 8 inches")
heightInInches = st.selectbox("Select Height in Inches", (0,1,2,3,4,5,6,7,8,9,10,11),index=None,placeholder= "Choose your height in Inches. eg, 5 foot '8 inches'")


weightInPounds = st.number_input("Please enter your weight in pounds")

try:
    heightInTotal = (heightInFeet * 12) + heightInInches
    BMI = round((weightInPounds /heightInTotal/heightInTotal) * 703, 2)

    if 0.1 <= BMI <= 18.4:
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
