import streamlit as st
import pandas as pd

#dataanalysis other

df = pd.read_csv('./data/data1.csv')
st.dataframe(df)
st.line_chart(df)
st.bar_chart(df['2022'])
