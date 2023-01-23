
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit.components.v1 import html


st.set_page_config(page_title="test 🧪", page_icon=":moneybag:",
                   layout="wide", initial_sidebar_state='collapsed')


# home button
if st.button('🏠 Home'):
    switch_page('Home')

st.markdown('# test 🧪')

code = '''<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3858220107949234"
     crossorigin="anonymous"></script>'''

#html(code)

st.markdown(code, unsafe_allow_html= True)

