import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Student Performance Data Analysis")

df = pd.read_csv("data.csv")

st.subheader("Dataset Preview")
st.write(df.head())

st.subheader("Missing Values")
st.write(df.isnull().sum())

st.subheader("Gender Distribution")

fig, ax = plt.subplots(figsize=(6,4))
sns.countplot(x='gender', data=df, ax=ax)

st.pyplot(fig)