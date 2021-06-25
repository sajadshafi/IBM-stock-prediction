import requests

params = {
    'apikey': "YALAP07WIB4QT1FX",
    'symbol': "IBM",
    'function': "TIME_SERIES_DAILY",
    'outputsize': "full"
}

base_api = 'https://www.alphavantage.co/query?'
response = requests.get(base_api, params = params)

result = response.json()

stcks = result["Time Series (Daily)"]


class my_dictionary(dict):
  
    # __init__ function
    def __init__(self):
        self = dict()
          
    # Function to add key:value
    def add(self, key, value):
        self[key] = value
        

        
data = []
for stck_key in stcks:
    
    dict_obj = my_dictionary()
    
    date = stck_key
    dict_obj.add('date', date)
    
    dicct = stcks[stck_key]
    
    for k in dicct:
        dict_obj.add(k, dicct[k])
    
    data.append(dict_obj)
    
    
import csv
import pandas as pd

# Create dataframe out of all the stocks
stocks_df = pd.DataFrame(data)

# Put that dataframe into an excel file
stocks_df.to_excel('stocks.xlsx', index = False)

'''
By default this code will make an excel file inside the folder to where it will be executed but we can also give it a path where we want to store it
'''

print("Done.")