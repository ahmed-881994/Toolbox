from streamlit_extras.switch_page_button import switch_page
import streamlit as st
from utils import encryptor_api
from htbuilder import a, img
# page config
st.set_page_config(page_title='Encryptor',
                   page_icon='#️⃣', layout='wide', initial_sidebar_state='collapsed')
# home button
if st.button('🏠 Home'):
    switch_page('Home')


# title
st.title("Encryptor #️⃣")
st.markdown('This tool was built as an easy way to encrypt messages used in treasure hunts for kids.')
badge_html = str(
    a(href=f"https://encryptorapi-3-e5583038.deta.app/docs")(
        img(
            src=f"https://img.shields.io/static/v1?label=Encryptor&message=docs&color=brightgreen&style=flat-square&logo=Swagger"
        )
    )
)
st.write('API: '+ badge_html, unsafe_allow_html=True)
# input text area
st.subheader("Plain text:")
plain_text_in = st.text_area(
    'Plain text', height=250, label_visibility='collapsed')

st.caption('*See examples below.')

# encryption method choice
method = st.radio('**Choose the encryption method:**',
                  ('Caesar', 'Morse', 'Numeric', 'Reverse numeric', 'NATO alphabet'), horizontal=True)

# language choice
if method == 'NATO alphabet':
    lang = None
    payload = {
    "plainText": plain_text_in,
    }
else:
    lang = st.radio('**Choose the language:**',
                ('EN', 'AR',), horizontal=True)
    payload = {
        "plainText": plain_text_in,
        "language": lang
    }

# shift selection
shift = None
if method == 'Caesar':
    if lang == 'EN':
        shift = st.slider('**Shift:**', 1, 26, 1)
    else:
        shift = st.slider('**Shift:**', 1, 28, 1)
    # payload changes if the method is caesar
    payload = {
        "plainText": plain_text_in,
        "language": lang,
        "shift": shift
    }

if st.button('Encrypt', type='primary'):
    with st.spinner(text="Encrypting..."):
        # call encryption API
        response = encryptor_api.encrypt(method, payload) #type: ignore
        # handle response
        if response.get('cypherText') is not None:
            st.subheader("Cypher:")
            st.code(body=response['cypherText'])
        elif response['detail'][0]['msg'] is not None:
            st.error(response['detail'][0]['msg'])
        else:
            st.error('An error occurred')
            

# examples
with st.expander("**See examples**"):
    st.subheader("Caesar")
    st.code(
        body='''Plain text: Hello world\nLanguage: EN\nShift: 1\nCypher: IFMMP XPSME''')
    st.subheader("Morse")
    st.code(body='''Plain text: Hello world\nLanguage: EN\nCypher: .... . .-.. .-.. ---/ .-- --- .-. .-.. -..''')
    st.subheader("Numeric")
    st.code(body='''Plain text: Hello world\nLanguage: EN\nCypher: 8 5 12 12 15/ 23 15 18 12 4''')
    st.subheader("Reverse numeric")
    st.code(body='''Plain text: Hello world\nLanguage: EN\nCypher: 19 22 15 15 12/ 4 12 9 15 23''')
    st.subheader("NATO alphabet")
    st.caption('English language only')
    st.code(body='''Plain text: Hello world\nCypher: hotel echo lima lima oscar (space) whiskey oscar romeo lima delta''')
