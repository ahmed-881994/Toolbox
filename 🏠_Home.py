import streamlit as st
from htbuilder import a, img, styles
from htbuilder.units import px
import streamlit_option_menu
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(page_title='Toolbox',
                   page_icon='🧰', layout='wide', initial_sidebar_state='collapsed')


st.title("Welcome 👋")
#st.write('''This is a collection of several tools I\'ve made over the years, 
#        whether for a specific need or just to practice **Python** while implementing tools I already use.''')
selected=streamlit_option_menu.option_menu(menu_title='Tools', options= ['Home', 'Encryptor', 'CurrEx', 'Base64 to PDF', 'Formatter'],menu_icon='tools',icons=['house','hash','currency-exchange','file-earmark-pdf','list-columns-reverse'],orientation='horizontal', default_index=0)

if selected != 'Home':
    switch_page(selected)
    

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

st.write('<br/>'+ github_link_html + ' ' + linkedin_link_html, unsafe_allow_html=True)