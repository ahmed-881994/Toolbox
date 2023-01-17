from streamlit_extras.switch_page_button import switch_page
import streamlit as st

# page config
st.set_page_config(page_title='JSON formatter',
                   page_icon='{...}', layout='wide', initial_sidebar_state='collapsed')

# home button
if st.button('🏠 Home'):
    switch_page('Home')

# title
st.markdown("# JSON formatter {...}")

# declare columns
col1, col2 = st.columns(2)

with col1:
    # input text area
    st.subheader("Input string:")
    input_string = st.text_area(
        'Plain text', height=500, label_visibility='collapsed')
    if st.button('Format', type='primary'):
        # output result
        with col2:
            st.subheader("JSON:")
            st.json(input_string)
