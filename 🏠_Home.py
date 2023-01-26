
import streamlit as st
from htbuilder import a, img, styles
from htbuilder.units import px

st.set_page_config(page_title='Toolbox',
                   page_icon='🧰', layout='wide', initial_sidebar_state='expanded')


if __name__ == "__main__":
    st.title("Welcome 👋")

    st.write('''This is a collection of several tools I\'ve made over the years, 
            whether for a specific need or just to practice **Python** while implementing tools I already use.''')
github_link_html = str(
    a(href='https://github.com/ahmed-881994', style=styles(margin=px(5)))(
        img(
            src='https://cdn.simpleicons.org/github', height=32, width=32, alt='Github', title='Github'
        )
    )
)

linkedin_link_html = str(
    a(href='https://www.linkedin.com/in/ahmed-safwat-eldamanhoury', style=styles(margin=px(5)))(
        img(
            src='https://cdn.simpleicons.org/linkedin', height=32, width=32, alt='Linkedin', title='Linkedin'
        )
    )
)

st.write(github_link_html + ' ' + linkedin_link_html, unsafe_allow_html=True)