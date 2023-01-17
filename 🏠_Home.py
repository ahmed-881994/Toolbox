
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.mention import mention
from streamlit_extras.badges import badge
from streamlit_extras.app_logo import add_logo


st.set_page_config(page_title='Toolbox',
                   page_icon='🧰', layout='wide', initial_sidebar_state='auto')


if __name__=="__main__":
    st.title("Welcome 👋")

    st.write('''This is a collection of several tools I\'ve made over the years, 
            whether for a specific need or just to practice **Python** while implementing tools I already use.''')
