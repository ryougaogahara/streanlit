# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd
import time

st.title("Web App")
st.write("**これがstreamlitアプリ**")

answer = st.button('Say hello')

if answer == True:
     st.write('Why hello there')
else:
     st.write('Goodbye')
    
data = {
    'lat': np.random.randn(100) / 100 + 35.68,
    'lon': np.random.randn(100) / 100 + 139.75,
}
map_data = pd.DataFrame(data)
# 地図に散布図を描く
st.map(map_data)



value = st.slider('Select a value', 0, 100, 50) # min max default


if st.button('start'):
     with st.spinner('conecting...'):
          time.sleep(3)
          st.write('end')
