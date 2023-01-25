import base64
import streamlit as st
from streamlit_extras.switch_page_button import switch_page


def is_base64(string):
    try:
        base64.b64decode(string)
        return True
    except:
        return False


# Page setup
st.set_page_config(page_title='Base64 to PDF',
                   page_icon='📄', layout='wide', initial_sidebar_state='collapsed')

# home button
if st.button('🏠 Home'):
    switch_page('Home')

st.title('Base64 to PDF 📄')
base64_in = st.text_area('**Base64:**', height=300)

# Handling input
if st.button('Decode', type='primary'):

    if base64_in == '' or base64_in is None:
        st.error('**No input found** :eyes:')
    elif not is_base64(base64_in):
        st.error('**Invalid base64 string** :confused:')
    else:
        st.success('**Success** ✅')
        # Embedding PDF in HTML
        pdf_display = F'<iframe  src="data:application/pdf;base64,{base64_in}" width="100%" height="800" type="application/pdf">'
        # Displaying File
        st.markdown(pdf_display, unsafe_allow_html=True)
