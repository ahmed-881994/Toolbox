import os
from datetime import date, timedelta
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

st.title('CurrEx 💱')

@st.cache(persist= True)
def load_data():
    # Load the data from the JSON file
    with open('./assets/currency_codes.json', 'r') as json_file:
        data = json.load(json_file)
    return data

# load currency data
curr_codes_data = load_data()
# add currency names to currency code
options = [curr_code+': '+curr_codes_data[curr_code]['name'] for curr_code in curr_codes_data]

# add ui elements
from_currency = st.selectbox("**Select a source currency**", options, key='from_curr')
to_currency = st.selectbox("**Select a target currency**", options, key='to_curr')
amount = st.number_input('**Enter value**')

# clean input
from_currency = str(from_currency)[:str(from_currency).index(':')]
to_currency = str(to_currency)[:str(to_currency).index(':')]

# call currenct converter api
convert_response_today = exchange_api.convert(from_currency, to_currency, amount)
convert_response_yesterday = exchange_api.convert_with_date(from_currency, to_currency, amount, date.today() - timedelta(1))

# calculate the delta from yesterday's price
rate_today =0 if convert_response_today['info']['rate'] is None else convert_response_today['info']['rate']
rate_yesterday=0 if convert_response_today['result'] is None else convert_response_yesterday['rates'][to_currency]
delta=rate_today-rate_yesterday

request_amt = 0 if convert_response_today['result'] is None else convert_response_today['query']['amount']
response_amt = 0 if convert_response_today['result'] is None else convert_response_today['result']

path = os.getcwd()
col1, col2 = st.columns(2)
# source currency column
with col1:
    from_flag = Image.open(path+curr_codes_data[from_currency]['icon'])
    st.image(from_flag)
    if request_amt == 0:
        st.metric(label=curr_codes_data[from_currency]['name'], value=request_amt, delta='', delta_color='off')
    else:
        st.metric(label=curr_codes_data[from_currency]['name'], value=request_amt, delta='', delta_color='off')

# target currency column
with col2:
    to_flag = Image.open(path+curr_codes_data[to_currency]['icon'])
    st.image(to_flag)
    if response_amt is None:
        st.metric(label=curr_codes_data[to_currency]['name'], value= response_amt, delta=delta, delta_color='inverse', help='arrows indicate change from yesterday\'s price')
    else:
        st.metric(label=curr_codes_data[to_currency]['name'], value= response_amt, delta=delta, delta_color='inverse', help='arrows indicate change from yesterday\'s price' )

style_metric_cards()
