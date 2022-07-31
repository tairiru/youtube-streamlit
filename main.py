import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from torch import layer_norm
import time
#---------------------------------------------
st.title('Streamlit')
st.write('Progresbar')
'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'Done!!'
#---------------------------------------------
st.write('Display Image')
img = Image.open('./data/super_moon.jpg')
st.image(img,caption='super_moon', use_column_width=True)
#---------------------------------------------
if st.checkbox('Show Image'):
    img = Image.open('./data/super_moon.jpg')
    st.image(img,caption='super_moon', use_column_width=True)
#---------------------------------------------
left_column,right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')
#---------------------------------------------
expander1 = st.beta_expander('問い合わせ1')
expander1.write('取り合わせ1の回答')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('取り合わせ2の回答')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('取り合わせ3の回答')
#---------------------------------------------

option = st.selectbox('あなたが好きな数字を教えてください。',
    list(range(1,11))  )
st.write('Interctive Widgets')
'あなたの好きな数字は、', option, 'です。'
text = st.text_input('あなたの趣味を教えてください。')
condition = st.slider('あながの今の調子は？', 0, 100, 50)
'あなたの趣味は:', text
'コンディション:', condition
#---------------------------------------------


#---------------------------------------------


#---------------------------------------------
image = Image.open('./data/button.png')
st.image(image, width=200)
#---------------------------------------------
df = pd.DataFrame({
    '１列目': [1, 2, 3, 4],
    '２列目': [10, 20, 30, 40]
})

"""
# 章
## 節
### 項

```Python
import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from torch import layer_norm

```

"""

st.dataframe(df.style.highlight_max(axis=0), width=500, height=300)

st.table(df.style.highlight_max(axis=0))
#---------------------------------------------

#---------------------------------------------
st.caption('This is apptest')

tab1, tab2 = st.tabs(["graph", "data"])
data = np.random.randn(10,3)

with tab1:
    st.subheader("graph")
    st.line_chart(data)
with tab2:
    st.subheader("data")
    st.dataframe(data)

image = Image.open('./data/button.png')
st.image(image, width=200)