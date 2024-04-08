import streamlit as st
import folium
from streamlit_folium import folium_static

st.title("HCI Final Project about Health (Working title)")

heightInFeet = st.selectbox("Select Height in Feet", (3, 4, 5, 6, 7, 8),placeholder= "Choose your height in Feet. eg '5 foot' 8 inches")
heightInInches = st.selectbox("Select Height in Inches", (0,1,2,3,4,5,6,7,8,9,10,11),placeholder= "Choose your height in Inches. eg 5 foot '8 inches'")
weightInPounds = st.number_input("Please enter your weight in pounds")

heightInFeet = int(heightInFeet)
heightInInches = int(heightInInches)
heightInTotal = (heightInFeet * 12) + heightInInches

BMI =(weightInPounds /heightInTotal/heightInTotal) * 703
st.success("Your BMI is " + str(BMI))