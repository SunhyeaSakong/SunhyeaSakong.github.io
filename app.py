import streamlit as st 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Hogwarts Data Explorer")
uploaded_file = st.file_uploader("dataset_train.csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    x = st.selectbox("X-axis", df.columns)
    y = st.selectbox("Y-axis", df.columns)
    if 'Hogwarts House' in df.columns:
        sns.scatterplot(data=df, x=x, y=y, hue="Hogwarts House")
        st.pyplot(plt)
