import streamlit as st
import pandas as pd
import numpy as np

# -------------------------------
# 🏠 Basic Streamlit App UI
# -------------------------------
st.title("My Streamlit App")
st.header("Introduction")
st.subheader("A Subheading")

st.write("This is some plain text.")
st.markdown("This is *bold* text using Markdown")
st.code("print('Hello, Streamlit!')", language="python")

# -------------------------------
# 🧍‍♂️ User Interaction Widgets
# -------------------------------
user_input = st.text_input("Enter your name:")
if user_input:
    st.write(f"Hello, {user_input}!")

age = st.slider("Select your age:", 0, 100, 25)
st.write(f"You are {age} years old.")

if st.button("Click me!"):
    st.success("Button clicked!")

agree = st.checkbox("I agree to the terms and conditions.")
if agree:
    st.info("✅ Great! You agreed to the terms.")

# -------------------------------
# 📁 File Upload and Text Area
# -------------------------------
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.success("File uploaded successfully!")

long_text = st.text_area("Enter a long message:")
if long_text:
    st.write("You entered:", long_text)

# -------------------------------
# 📊 Basic Charts Section
# -------------------------------
st.header("📈 Basic Streamlit Charts")

# Create some sample data
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

# Display the dataframe
st.subheader("Data Table")
st.dataframe(data)

# Line chart
st.subheader("Line Chart")
st.line_chart(data)

# Area chart
st.subheader("Area Chart")
st.area_chart(data)

# Bar chart
st.subheader("Bar Chart")
st.bar_chart(data)
