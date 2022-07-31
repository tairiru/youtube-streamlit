import streamlit as st
import numpy as np
import pandas as pd

st.title('chart')

st.write('ChartFrame')

df = pd.DataFrame(
    np.random.rand(21, 3),
    columns=['a', 'b', 'c']
)

st.dataframe(df)

st.line_chart(df)

st.area_chart(df)

st.bar_chart(df)