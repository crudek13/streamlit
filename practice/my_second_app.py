'''
conda activate env_streamlit
'''


# Import packages
import streamlit as st
import pandas as pd
import numpy as np


##### Streamlit App #####


# Title of the app
st.title("My Enhanced Streamlit App")

# Adding a header
st.header("Welcome to Streamlit")

# Adding some text
st.text("This is a simple Streamlit app with more features")

# Creating an input box
user_input = st.text_input("Enter your name", "")

# Displaying the input
if user_input:
    st.write(f"Hello, {user_input}!")

# Adding a slider
age = st.slider("Select your age", 0, 100, 25)
st.write(f"Your age is: {age}")

# Adding a button
if st.button("Click me"):
    st.write("Button clicked!")

# Creating a simple DataFrame
data = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y']
)

# Adding a line chart
st.line_chart(data)