import streamlit as st
import pandas as pd
import plotly.express as px

st.title("In search for happiness")
x_axis = st.selectbox("Select the data for the X-axis",
                      ("GDP", "Happiness", "Generosity", "Corruption"))
y_axis = st.selectbox("Select the data for the Y-axis",
                      ("GDP", "Happiness", "Generosity", "Corruption"))
st.subheader(f"{x_axis} and {y_axis}")

df = pd.read_csv("happy.csv")

x_axis = x_axis.lower()
y_axis= y_axis.lower()

figure = px.scatter(x=df[x_axis], y=df[y_axis],
                    labels={"x": x_axis, "y": y_axis})
st.plotly_chart(figure)
