import streamlit as st
from sentiment_engine import sentiment_analyzer


def hello():
    st.header("InstantCat")
    greeting = st.text_input("Hello, how are you?")
    if sentiment_analyzer(greeting) > 0:
        st.write("I am glad you are okay :smile:") 
    elif sentiment_analyzer(greeting) == 0:
        st.write("Things can be better.:sunglasses:")

    else:
        st.write("Don't worry:sad:")
hello()