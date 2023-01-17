import json
    
def appeadd_latest_ratend(currency, date, buy, sell):
    # open file and load data
    with open('exchange_rates.json', 'r') as json_file:
        history_data = json.load(json_file)
    # append latest exchange rate to selected currency
    history_data[currency]['dates'].append({'date': date, 'buy': buy, 'sell': sell})
    # write new data to file
    with open('exchange_rates.json', 'w') as json_file:
        json.dump(history_data, json_file, indent=4)
        

    
    
    