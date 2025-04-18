import streamlit as st
import pandas as pd
st.title("Bmi calculator app")
st.write("This app calculates your BMI based on your height and weight.")
height = st.slider ("Enter your height (in cm): " ,100,250,170)
weight = st.slider ("Enter your height (in kg): " ,40 ,200,70)
bmi = weight / ((height / 100) ** 2)

st.write(f"Your BMI is :,{bmi:.2f}")

st.write("BMI categories:")
st.write("Underweight: BMI < 18.5")
st.write("Normal weight: BMI 18.5 - 24.9")
st.write("Overweight: BMI 25 - 29.9")
st.write("Obesity: BMI >= 30")
if bmi < 18.5:
    st.write("You are underweight.")
elif 18.5 <= bmi < 24.9:
    st.write("You have a normal weight.")
elif 25 <= bmi < 29.9:
    st.write("You are overweight.")
else:
    st.write("You are obese.")
st.write("This app is built By Rizwan Ahmed Shar.")