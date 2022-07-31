import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame(
    np.random.rand(101, 2)/[50, 50]+[35.69, 139.70],
    columns=['lat','lon']#緯度経度
)

st.map(df)