from streamlit_extras.switch_page_button import switch_page
import streamlit as st
from xml.dom import minidom

def format_xml(xml_string):
    # parse the XML string and return formatted XML string
    xml_dom = minidom.parseString(xml_string)
    formatted_xml = xml_dom.toprettyxml()
    return formatted_xml

# page config
st.set_page_config(page_title='formatter',
                   page_icon='{...}', layout='wide', initial_sidebar_state='collapsed')

# home button
if st.button('🏠 Home'):
    switch_page('Home')

# title
st.title("Formatter {...}")

# declare tabs
tab1, tab2 = st.tabs(['**JSON**', '**XML**'])

with tab1:
    # declare columns
    col1, col2 = st.columns(2)
    with col1:
        # input text area
        st.subheader("Input:")
        input_string = st.text_area(
            'Plain text', height=450, label_visibility='collapsed', key='JSON_input')
        if st.button('Format', type='primary', key='JSON_format_button'):
            # output result
            with col2:
                st.subheader("JSON:")
                st.json(input_string)


with tab2:
    # declare columns
    col1, col2 = st.columns(2)
    with col1:
        # input text area
        st.subheader("Input:")
        input_string = st.text_area(
            'Plain text', height=450, label_visibility='collapsed', key='XML_input')
    if st.button('Format', type='primary', key='XML_format_button'):
        # output result
        with col2:
            st.subheader("XML:")
            st.code(format_xml(input_string), language='xml-doc')

