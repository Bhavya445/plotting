import streamlit as st
import plotly.express as px
import pandas as pd

data = pd.read_csv("happy.csv")

st.title("In Search for Happiness")
#st.write(data)
data_x = st.selectbox("Select the data for the X-axis",tuple(data.columns))
data_y = st.selectbox("Select the data for the Y-axis",tuple(data.columns))
st.subheader(f"{data_x} and {data_y}")

figure = px.scatter(x=data[data_x], y=data[data_y],labels={"x":data_x,"y":data_y})
st.plotly_chart(figure)