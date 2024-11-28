import pandas as pd
import streamlit as st
 
st.title('Hello, Streamlit!')
 
feedback = None


col1, col2, _ = st.columns([1,1,8]) # 比率を指定
# col1, col2 = st.columns(2) # 個数のみ指定
 
if col1.button('<img draggable="false" role="img" class="emoji" alt="👍" src="https://s.w.org/images/core/emoji/14.0.0/svg/1f44d.svg">'):
    feedback = 'positive'
 
if col2.button('<img draggable="false" role="img" class="emoji" alt="👎" src="https://s.w.org/images/core/emoji/14.0.0/svg/1f44e.svg">'):
    feedback = 'negative'
 
if feedback:
    st.write(f'You selected {feedback} feedback.')
