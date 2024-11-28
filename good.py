import streamlit as st

st.title('Hello, Streamlit!')

feedback = None

col1, col2, _ = st.columns([1, 1, 8])  # 比率を指定

# col1に絵文字のボタンを表示
if col1.button('👍'):
    feedback = 'positive'

# col2に絵文字のボタンを表示
if col2.button('👎'):
    feedback = 'negative'

# フィードバックが選択された場合、その内容を表示
if feedback:
    st.write(f'You selected {feedback} feedback.')
