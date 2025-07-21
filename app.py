import streamlit as st 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Hogwarts Data Explorer")
uploaded_file = st.file_uploader("Upload your csv file", type=["csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("### Dataset Preview")
    st.dataframe(df.head())

    if 'Hogwarts House' in df.columns:
        x = st.selectbox("X-axis", df.columns)
        y = st.selectbox("Y-axis", df.columns)

        st.write(f"### Scatterplot: {x} vs {y} by House")
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x, y=y, hue="Hogwarts House", ax=ax)
        st.pyplot(fig)
    else:
        st.warning("Your dataset must contain "Hogwarts House" colomn for this plot.")
       
