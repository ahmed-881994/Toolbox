import os
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_card import card
import json
from utils import exchange_api
from PIL import Image

st.set_page_config(page_title="CurrEx 💱", page_icon=":moneybag:",
                   layout="wide", initial_sidebar_state='collapsed')


# home button
if st.button('🏠 Home'):
    switch_page('Home')

st.markdown('# CurrEx 💱')

@st.cache(persist= True)
def load_data():
    # Load the data from the JSON file
    with open('./assets/currency_codes.json', 'r') as json_file:
        data = json.load(json_file)
    return data


data = load_data()

# Show the available currencies
currencies = list(data.keys())
from_currency = st.selectbox("**Select a source currency**", currencies, key='from_curr')
to_currency = st.selectbox("**Select a target currency**", currencies, key='to_curr')
amount = st.number_input('**Enter value**')

response = exchange_api.convert(from_currency, to_currency, amount)

path = os.getcwd()

col1, col2 = st.columns(2)
from_flag = Image.open(path+data[from_currency]['icon'])
col1.image(from_flag)
col1.metric(label=data[from_currency]['name'], value="{:.2f}".format(float(amount)), delta='', delta_color='off')

to_flag = Image.open(path+data[to_currency]['icon'])
col2.image(to_flag)
response_amt = response['result']
if response_amt is None:
    response_amt = 0
col2.metric(label=data[to_currency]['name'], value= "{:.2f}".format(float(response_amt)), delta='', delta_color='off')
style_metric_cards()
