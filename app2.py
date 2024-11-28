import streamlit as st
from PIL import Image
img = Image.open('gori.jpg')
st.image(img)
