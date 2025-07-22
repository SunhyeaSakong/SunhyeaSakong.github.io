import streamlit as st 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Hogwarts Data Explorer")

uploaded_file = st.file_uploader("Upload your csv file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("### Dataset Preview")
    st.dataframe(df.head())

    numeric_cols = df.select_dtypes(include='number).columns.tolist()

    if 'Hogwarts House' in df.columns and in numeric_cols:
        x = st.selectbox("Select X-axis", numeric_cols)
        y = st.selectbox("Select y-axis", numeric_cols)

        st.write(f"### Scatterplot: {x} vs {y} by House")
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x, y=y, hue="Hogwarts House", ax=ax)
        st.pyplot(fig)
    elif 'Hofwarts House' not in df.columns:
        st.Warning("Your dataset contain 'Hogwarts House' colomn for this plot.")
    else:
        st.warning("Your dataset must contain numeric columns for plotting.")
       
